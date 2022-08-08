import enum
from pydantic import BaseModel
from typing import Any, List, Literal, NamedTuple, Optional, Tuple, TypeVar, Union
from ..scraper.html_parser.grammar_tty import TagsTty
from __future__ import annotations

class DataHTML(BaseModel):
    pass

    @classmethod
    def default(cls) -> DataHTML:
        return cls()