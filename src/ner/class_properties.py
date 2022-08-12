from __future__ import annotations

import re
from curses.ascii import isalnum, isdigit, islower, isupper
from enum import Enum
from itertools import combinations, zip_longest
from operator import countOf
from typing import List, Tuple

from pydantic import BaseModel

from .currency_signs import currency_signs


class NERTtyProperties(BaseModel):
    text: str
    paragraph: str
    is_capitalized: bool = False
    contains_only_one_capital: bool = False
    all_capitals_and_period: bool = False
    contains_a_digit: bool = False
    more_than_2_digit: bool = False
    more_than_4_digit: bool = False
    only_digit_and_slash: bool = False
    contains_currency_sign_at_start_end: bool = False
    contains_percent_sign_at_start_end: bool = False
    contains_all_digit_and_period: bool = False
    sequence_of_caps: bool = False
    unique_in_doc: bool = False

    @classmethod
    def new(cls, text: str, paragraph: str) -> NERTtyProperties:
        obj = cls(text=text, paragraph=paragraph)
        obj.assert_is_cap()
        obj.assert_contains_only_one_cap()
        obj.assert_all_capital_and_period()
        obj.assert_contains_a_digit()
        obj.assert_has_more_than_two_digits()
        obj.assert_has_more_than_four_digits()
        obj.assert_all_digits_and_slash()
        obj.assert_contains_cs_at_start_end()
        obj.assert_contains_pa_at_start_end()
        obj.assert_is_digit_or_period()
        obj.assert_is_sequence_of_caps()
        obj.assert_unique_in_doc()

        return obj
    
    def assert_is_cap(self):
        if self.text[0].isupper():
            self.is_capitalized = True

    def assert_contains_only_one_cap(self):
        self.contains_only_one_capital = len([
            c.isupper() for c in self.text
        ]) == 1

    def assert_all_capital_and_period(self):
        self.all_capitals_and_period = all([
            c.isdigit() or c == '.' for c in self.text
        ])

    def assert_contains_a_digit(self):
        if self.text.isalnum:
            self.contains_a_digit = True

    def assert_has_more_than_two_digits(self):
        self.more_than_2_digit = len([
            c.isdigit() for c in self.text
        ]) > 2

    def assert_has_more_than_four_digits(self):
        self.more_than_4_digit = len([
            c.isdigit() for c in self.text
        ]) > 4

    def assert_all_digits_and_slash(self):
        self.only_digit_and_slash = all([
            c.isdigit() or c == '/' for c in self.text
        ])

    def assert_contains_cs_at_start_end(self):
        start_letter = self.text[0]
        end_letter = self.text[-1]

        symbols_flattened = sum(currency_signs, [])

        if any([l in symbols_flattened for l in 
                    [start_letter, end_letter]]):
            self.contains_currency_sign_at_start_end = True

    def assert_contains_pa_at_start_end(self):
        start_letter = self.text[0]
        end_letter = self.text[-1]

        if any([l == '%' for l in [
            start_letter, end_letter
        ]]):
            self.contains_percent_sign_at_start_end = True


    def assert_is_digit_or_period(self):
        self.contains_all_digit_and_period = all([
            c.isdigit() or c == '.' for c in self.text
        ])

    def assert_is_sequence_of_caps(self):
        if self.text[0].islower():
            return
        
        words_split = re.split(r"\s+", self.paragraph)

        bigrams = combinations(words_split, 2)
        trigrams = combinations(words_split, 3)
        quadgrams = combinations(words_split, 3)
        quingrams = combinations(words_split, 3)

        def assert_has_text_and_is_all_cap(tp: Tuple) -> bool:
            if tp is None:
                return False

            if self.text not in tp:
                return False

            return all([w[0].isupper() for w in tp])

        for bi, tri, quad, quin in zip_longest(
            bigrams, trigrams, quadgrams, quingrams
        ):
            for tp in [bi, tri, quad, quin]:
                if assert_has_text_and_is_all_cap(tp):
                    self.sequence_of_caps = True
                    break

    def assert_unique_in_doc(self):
        self.unique_in_doc = countOf(self.paragraph, self.text) == 1
