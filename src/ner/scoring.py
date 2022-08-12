from __future__ import annotations

from enum import Enum
from typing import List, Tuple

from pydantic import BaseModel

from .class_properties import NERTtyProperties


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

    def __eq__(self, other: ScoreProb) -> bool:
        return self.score == other.score and self.prob == other.prob

    def score_equal(self, other: ScoreTty) -> bool:
        return self.score == other


class NERTty(int, Enum):
    NotEntity = -1
    Person = 0
    Place = 1
    DateTime = 2
    Organization = 3
    Currency = 4
    Percentage = 5


class SPW(BaseModel):
    score_probs: List[ScoreProb]
    ner_class: NERTty

    @classmethod
    def new(
        cls,
        scores_probs: List[Tuple[ScoreTty, int]],
        ner_class: NERTty,
    ):
        if sum(b[1] for b in scores_probs) > 100:
            raise Exception(f"Error with probs: {ner_class}")

        sp = [ScoreProb(score=s, prob=p)
              for s, p
              in scores_probs]

        obj = SPW(score_probs=sp, ner_class=ner_class)

        return obj


PERSON = SPW.new(
    [
        (ScoreTty.new(cap_score=1), 40),
        (ScoreTty.new(digit_score=0), 15),
        (ScoreTty.new(signage_score=0), 15),
        (ScoreTty.new(context_score=1), 30),
    ],
    NERTty.Person
)

PLACE = SPW.new(
    [
        (ScoreTty.new(cap_score=1), 10),
        (ScoreTty.new(cap_score=3), 10),
        (ScoreTty.new(cap_score=4), 5),
        (ScoreTty.new(digit_score=2), 5),
        (ScoreTty.new(digit_score=4), 10),
        (ScoreTty.new(digit_score=9), 5),
        (ScoreTty.new(digit_score=11), 5),
        (ScoreTty.new(context_score=1), 20),
        (ScoreTty.new(context_score=2), 5),
        (ScoreTty.new(context_score=3), 15),
    ],
    NERTty.Place
)

DATETIME = SPW.new(
    [
        (ScoreTty.new(cap_score=4), 15),
        (ScoreTty.new(digit_score=2), 10),
        (ScoreTty.new(digit_score=4), 10),
        (ScoreTty.new(digit_score=9), 5),
        (ScoreTty.new(digit_score=11), 40),
        (ScoreTty.new(context_score=1), 5),
        (ScoreTty.new(context_score=2), 5),
        (ScoreTty.new(context_score=3), 5),
    ],
    NERTty.DateTime
)
ORGANIZATION = SPW.new(
    [
        (ScoreTty.new(cap_score=4), 60),
        (ScoreTty.new(context_score=1), 20),
        (ScoreTty.new(context_score=2), 10),
        (ScoreTty.new(context_score=3), 10),
    ],
    NERTty.Organization
)
CURRENCY = SPW.new(
    [
        (ScoreTty.new(signage_score=1), 100),
    ],
    NERTty.Currency
)
PERCENTAGE = SPW.new(
    [
        (ScoreTty.new(signage_score=2), 100),
    ],
    NERTty.Percentage
)


def unwrap_temps() -> List[SPW]:
    return [
        PERSON,
        PLACE,
        DATETIME,
        ORGANIZATION,
        CURRENCY,
        PERCENTAGE
    ]


class NERScoreEntity(BaseModel):
    base: NERTtyProperties
    score: ScoreTty

    @classmethod
    def new(cls, text: str, context: str) -> NERScoreEntity:
        properties = NERTtyProperties.new(text, context)
        dummy_score = ScoreTty(
            cap_score=0,
            digit_score=0,
            signage_score=0,
            context_score=0
        )

        obj = NERScoreEntity(
            base=properties,
            score=dummy_score
        )

        obj.calculate_score()

        return obj

    def calculate_score(self):
        def is_cap(x): return 1 if x.is_capitalized else 0
        def one_cap(x): return 2 if x.contains_only_one_capital else 0
        def all_cap_per(x): return 4 if x.all_capitals_and_period else 0
        def a_digit(x): return 1 if x.contains_a_digit else 0
        def two_digit(x): return 2 if x.more_than_2_digit else 0
        def four_digit(x): return 4 if x.more_than_4_digit else 0
        def only_d_an_s(x): return 7 if x.only_digit_and_slash else 0
        def curr(x): return 1 if x.contains_currency_sign_at_start_end else 0
        def per(x): return 2 if x.contains_percent_sign_at_start_end else 0
        def seq_caps(x): return 1 if x.sequence_of_caps else 0
        def unique(x): return 2 if x.unique_in_doc else 0

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

    def assert_ner_class(self) -> NERTty:
        spws = unwrap_temps()

        res = []

        for spw in spws:
            score_probs = spw.score_probs
            ner_class = spw.ner_class
            res_inner = (ner_class, 0)

            for sc_pr in score_probs:
                if sc_pr.score_equal(self.score):
                    res_inner[1] += sc_pr.prob

            res.append(res_inner)

        mx = max(res, key=lambda x: x[1])

        if mx < 15:
            return NERTty.NotEntity

        return mx
