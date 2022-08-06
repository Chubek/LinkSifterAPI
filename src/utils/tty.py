from pydantic import BaseModel
from enum import Enum
from typing import Dict, List, Literal, Optional, Tuple, Union, Any


class LinkTty(BaseModel):
    href: str
    text: str

class ParagraphTty(BaseModel):
    headings: List[str]
    bodies: List[str]
    
class MenuTty(BaseModel):
    length: int
    links: List[LinkTty]

class ControlFieldTypeTtty(int, Enum):
    RadioButton = 0
    EditField = 1
    CheckBox = 2
    ComboBox = 3
    ListBox = 4
    Button = 5

class ControlFieldTty(BaseModel):
    field_type: ControlFieldTypeTtty
    field_label: Optional[str] = None
    field_name: Optional[str] = None
    field_members_num: Optional[int] = 0
    default_checked: Optional[Union[Literal[True], Literal[False]]]


class ImageTty(BaseModel):
    src: str
    alt: Optional[str] = None
    size: Optional[Tuple[int, int]] = (0, 0)

class TableTty(BaseModel):
    size: Tuple[int, int]
    headings: List[str]
    items: Dict[str, List[str]]

class ListModeTty(int, Enum):
    Numbered = 0
    NotNumbered = 1 

class ListTty(BaseModel):
    num_items: int
    items: List[str]
    list_mode: ListModeTty

class StartPageScriptTty(str, Enum):
    DOMContentLoaded = "DOMContentLoaded"
    Load = "Load"

class PageKickOffScript(BaseModel):
    type: StartPageScriptTty
    script: str