from importlib.resources import contents
import json
from pydantic import BaseModel
from __future__ import annotations
from typing import Dict, List, Optional
from .grammars import TagsTty
from enum import Enum
from ...data_structures.parsed_map import ParsedMap


class NERTty(int, Enum):
    pass


class InnerText(BaseModel):
    text: str
    ner: NERTty


class HTMLContentParent(BaseModel):
    tag_type: TagsTty
    inner_text: Optional[str]
    tag_cls: Optional[List[str]] = []
    tag_id: Optional[str] = ""
    tag_raw: str


class ATagHtmlContent(HTMLContentParent):
    href: str


class DecoratorTagHtmlContent(HTMLContentParent):
    pass


class ListTty(int, Enum):
    Numbered = 0
    NotNumbered = 0


class ListTagHtmlContent(HTMLContentParent):
    list_type: ListTty
    number_of_items: int


class InputTty(int, Enum):
    Button = 0
    Checkbox = 1
    Color = 2
    Date = 3
    DateTimeLocal = 4
    Email = 5
    File = 6
    Hidden = 7
    Image = 8
    Month = 9
    Number = 10
    Password = 11
    Radio = 12
    Range = 13
    Submit = 15
    Tel = 16
    Text = 17
    Time = 18
    Url = 19
    Week = 20


class InputTagHtmlContent(HTMLContentParent):
    for_attr: Optional[str]
    value: Optional[str]
    readonly: bool = False
    diabled: bool = False
    size: int = 0
    maxlen: int = 0
    minimum: int = 0
    maximum: int = 0
    multiple = bool = 0
    placeholder: Optional[str]
    step: int = 0
    tty: InputTty


class ButtonTty(int, Enum):
    Submit = 0
    Button = 1
    Reset = 2


class ButtonTagHtmlContent(HTMLContentParent):
    name: Optional[str]
    type: ButtonTty = ButtonTty.Button
    value: str


class TableTagHtmlContent(HTMLContentParent):
    headers: List[str]
    num_cols: int
    num_rows: int
    containments: Dict[str, List[str]]


class HeadingTagHtmlContent(HTMLContentParent):
    pass


class AbbrTagHtmlContent(HTMLContentParent):
    title: Optional[str]


class HTMLParsedNode(BaseModel):
    key: int
    contents: HTMLContentParent

    def __str__(self) -> str:
        idd = self.contents.tag_id
        cls = "_".join(self.contents.tag_cls)

        return f"{idd}{cls}"


