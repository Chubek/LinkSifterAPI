from enum import Enum
from pydantic import BaseModel
from typing import Any, List, Literal, NamedTuple, Optional, Tuple, TypeVar, Union
from ..scraper.html_parser.grammar_tty import TagsTty
from __future__ import annotations
from ..ner.scoring import NERTty



class InnerText(BaseModel):
    text: str
    ner: NERTty


class DataHTML(BaseModel):
    tag_name: TagsTty = TagsTty.null


    @classmethod
    def default(cls) -> DataHTML:
        return cls()