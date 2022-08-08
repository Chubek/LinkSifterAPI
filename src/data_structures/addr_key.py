import enum
import json
from pydantic import BaseModel
from typing import Any, List, Literal, NamedTuple, Optional, Tuple, TypeVar, Union
from ..scraper.html_parser.grammar_tty import TagsTty


class AddrKey(BaseModel):
    tag: str = "global"
    cls_sorted: List[str] = ["no_class"]
    id: str = "default"
    number: int


    def __str__(self) -> str:
        cls_joined = "_".join(self.cls_sorted)
        idd = self.id
        tag = self.tag
        num = self.number

        return f"{tag}_{cls_joined}_{idd}_{num}"


    def __repr__(self) -> str:
        return json.dumps(self.todict())
