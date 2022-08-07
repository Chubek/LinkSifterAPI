
from pydantic import BaseModel
from typing import Any, List, Literal, Optional, Tuple, Union
from __future__ import annotations
from utils import simple_hasher
from .lexer_items import *

class Attribute(BaseModel):
    attr_name: str
    attr_value: str


class Text(BaseModel):
    text: List[SmallLetters]

class Element(BaseModel):
    tag_name: str
    attributes: List[Attribute]
    children: List[Union[Element, Text]]


class Parent(BaseModel):
    children: List[Union[Element, Text]]


class HASTParser:
    def __init__(self, text: str) -> None:
        self.text = text
        self.parent = Parent(children=[])
        self.end_level_reached = False
        self.current_element = None
        self.text_index = 1

    def recurse_tree(self):
        self.current_element = Element(
            tag_name="",
            attributes=[],
            children=[]
        )

        prev_char = self.text[self.text_index - 1]
        curr_char = self.text[self.text_index]
        next_char = self.text[self.text_index + 1]


