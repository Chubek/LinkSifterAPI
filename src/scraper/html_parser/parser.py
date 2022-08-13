from __future__ import annotations

import json
from enum import Enum
from importlib.resources import contents
from typing import Dict, List, Optional

from pydantic import BaseModel

from ...data_structures.htrie import HTrie
from .addr_key import AddrKey
from .data_html import DataHTML
from .grammars import TagsTty
from .lexer_items import *


class ListTty(int, Enum):
    Numbered = 0
    NotNumbered = 0



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



class HTMLParser:
    root = HTrie()
    
