from __future__ import annotations
from ast import Add

from enum import Enum
from typing import (Any, List, Literal, NamedTuple, Optional, Tuple, TypeVar,
                    Union)

from pydantic import BaseModel

from ...ner.scoring import NERTty
from .grammar_tty import TagsTty
from .addr_key import AddrKey

class InnerText(BaseModel):
    text: str
    ner: NERTty


class Attr(BaseModel):
    attr_name: str
    attr_value: Optional[Any]


class DataHTML(BaseModel):
    addr_key: AddrKey = AddrKey.new_default()
    inner_text: Optional[InnerText]
    attributes: List[Attr]


    @classmethod
    def default(cls) -> DataHTML:
        return cls()
