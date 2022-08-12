from typing import List, Tuple
from pydantic import BaseModel
from class_properties import NERClassProperties
from enum import Enum
from __future__ import annotations

class ScoreTty(BaseModel):
    cap_score: int
    digit_score: int
    signage_score: int
    context_score: int

    @classmethod
    def new(
        cls, 
        cap_score=0, 
        digit_score=0, 
        signage_score=0, 
        context_score=0
    ) -> ScoreTty:
        return ScoreTty(
            cap_score=cap_score,
            digit_score=digit_score,
            signage_score=signage_score,
            context_score=context_score
        )

    def unwrap(self) -> List[int]:
        return [
            self.cap_score,
            self.digit_score,
            self.signage_score,
            self.context_score
        ]

    def __eq__(self, other: ScoreTty) -> bool:
        return all([a == b for
                    a, b in
                    zip(
                        self.unwrap(),
                        other.unwrap()
                    )
        ])



class ScoreProb(BaseModel):
    score: ScoreTty
    prob: int


class NERClass(int, Enum):
    Person = 0
    Place = 1
    DateTime = 2
    Organization = 3
    Currency = 4
    Percentage = 5


class SPW(BaseModel):
    score_probs: List[ScoreProb]
    ner_class: NERClass


    @classmethod
    def new(
        cls,
        scores_probs: List[Tuple[ScoreTty, int]],
        ner_class: NERClass,
    ):
        if sum(b[1] for b in scores_probs) > 100:
            raise Exception("Error with probs")

        sp = [ScoreProb(score=s, prob=p)
                for s, p
                    in scores_probs]

        obj = SPW(score_probs=sp, ner_class=ner_class)

        return obj



class ScoreNerProbs(SPW, Enum):
    Person = SPW.new(
        [
            (ScoreTty.new(cap_score=1), 40),
            (ScoreTty.new(digit_score=0), 15),
            (ScoreTty.new(signage_score=0), 15),
            (ScoreTty.new(context_score=1), 30),
        ],
        NERClass.Person
    ),
    Place = SPW.new(
        [
            (ScoreTty.new(cap_score=1), 20),
            (ScoreTty.new(cap_score=3), 10),
            (ScoreTty.new(cap_score=4), 5),
            (ScoreTty.new(digit_score=1), 0),
            (ScoreTty.new(digit_score=2), 5),
            (ScoreTty.new(digit_score=4), 20),
            (ScoreTty.new(digit_score=9), 5),
            (ScoreTty.new(digit_score=11), 5),
            (ScoreTty.new(context_score=1), 20),
            (ScoreTty.new(context_score=2), 5),
            (ScoreTty.new(context_score=3), 15),
        ],
        NERClass.Place      
    )
    DateTime = SPW.new(
        [
            (ScoreTty.new(cap_score=4), 15),
            (ScoreTty.new(digit_score=1), 0),
            (ScoreTty.new(digit_score=2), 10),
            (ScoreTty.new(digit_score=4), 20),
            (ScoreTty.new(digit_score=9), 10),
            (ScoreTty.new(digit_score=11), 40),
            (ScoreTty.new(context_score=1), 5),
            (ScoreTty.new(context_score=2), 5),
            (ScoreTty.new(context_score=3), 5),
        ],
        NERClass.DateTime      
    )
    Organization = SPW.new(
        [
            (ScoreTty.new(cap_score=4), 60),
            (ScoreTty.new(context_score=1), 20),
            (ScoreTty.new(context_score=2), 10),
            (ScoreTty.new(context_score=3), 10),
        ],        
    )
    Currency = SPW.new(
        [
            (ScoreTty.new(signage_score=1), 100),
        ],
        NERClass.Currency       
    )
    Percentage = SPW.new(
        [
            (ScoreTty.new(signage_score=2), 100),
        ],
        NERClass.Percentage      
    )

    def unwrap(self) -> List[ScoreNerProbs]:
        return [
            self.Person,
            self.Place,
            self.DateTime,
            self.Organization,
            self.Currency,
            self.Percentage
        ]


    

class NERScoreEntity(BaseModel):
    base: NERClassProperties
    score: ScoreTty

    def calculate_score(self):
        is_cap = lambda x: 1 if x.is_capitalized else 0
        one_cap = lambda x: 2 if x.contains_only_one_capital else 0
        all_cap_per = lambda x: 4 if x.all_capitals_and_period else 0
        a_digit = lambda x: 1 if x.contains_a_digit else 0
        two_digit = lambda x: 2 if x.more_than_2_digit else 0
        four_digit = lambda x: 4 if x.more_than_4_digit else 0
        only_d_an_s = lambda x: 7 if x.only_digit_and_slash else 0
        curr = lambda x: 1 if x.contains_currency_sign_at_start_end else 0
        per = lambda x: 2 if x.contains_percent_sign_at_start_end else 0
        seq_caps = lambda x: 1 if x.sequence_of_caps else 0
        unique = lambda x: 2 if x.unique_in_doc else 0


        cap_score = sum([f(self.base)
                            for f in
                                [
                                    is_cap,
                                    one_cap,
                                    all_cap_per,
                                ]])

        digit_score = sum([f(self.base)
                            for f in
                                [
                                    a_digit,
                                    two_digit,
                                    four_digit,
                                    only_d_an_s
                                ]])
        
        signage_score = sum([f(self.base)
                            for f in
                                [
                                    curr,
                                    per,
                                ]])


        context_score = sum([f(self.base)
                            for f in
                                [
                                    seq_caps,
                                    unique,
                                ]])

        self.score = ScoreTty(
            cap_score=cap_score,
            digit_score=digit_score,
            signage_score=signage_score,
            context_score=context_score
        )

    def check_spw(self, spw: SPW) -> int:
        fin_prob = 0

        for scprob in spw.score_probs:
            score = scprob.score
            prob = scprob.prob

            if score == self.score:
                fin_prob += prob


        return fin_prob


    def assert_ner_class(self) -> NERClass:
        ner_probs = ScoreNerProbs.unwrap()

        res = []

        for ner_prob in ner_probs:
            res.append([
                ner_prob.ner_class,
                self.check_spw(ner_prob)
            ])


        return max(res, key=lambda x:x[1])

                    