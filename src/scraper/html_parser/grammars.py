from typing import List, Literal, Optional, Tuple
from .lexer_items import *  
from enum import Enum
from pydantic import BaseModel

class TagsTty(str, Enum):
    a = "a"
    p = "p"
    b = "b"
    i = "i"
    u = "u"
    q = "q"
    strong = "strong"
    ul = "ul"
    ol = "ol"
    li = "li"
    button = "button"
    input = "input"
    table = "table"
    tbody = "tbody"
    thead = "thead"
    tr = "tr"
    td = "td"
    th = "th"
    html = "html"
    body = "body"
    h1 = "h1"
    h2 = "h2"
    h3 = "h3"
    h4 = "h4"
    h5 = "h5"
    h6 = "h6"
    select = "select"
    abbr = "abbr"


class TagsSmallLetterTty(List[SmallLetters], Enum):
    a = [SmallLetters.a]
    p = [SmallLetters.p]
    b = [SmallLetters.b]
    i = [SmallLetters.i]
    u = [SmallLetters.u]
    q = [SmallLetters.q]
    strong = [
        SmallLetters.s,
        SmallLetters.t,
        SmallLetters.r,
        SmallLetters.o,
        SmallLetters.n,
        SmallLetters.g,
    ]
    ul = [
        SmallLetters.u,
        SmallLetters.l,
    ]
    ol = [
        SmallLetters.o,
        SmallLetters.l,
    ]
    li = [
        SmallLetters.l,
        SmallLetters.i,
    ]
    button = [
        SmallLetters.b,
        SmallLetters.u,
        SmallLetters.t,
        SmallLetters.t,
        SmallLetters.o,
        SmallLetters.n,
    ]
    input = [
        SmallLetters.i,
        SmallLetters.n,
        SmallLetters.p,
        SmallLetters.u,
        SmallLetters.t,
    ]
    table = [
        SmallLetters.t,
        SmallLetters.a,
        SmallLetters.b,
        SmallLetters.l,
        SmallLetters.e,
    ]
    tbody = [
        SmallLetters.t,
        SmallLetters.b,
        SmallLetters.o,
        SmallLetters.d,
        SmallLetters.y,
    ]
    thead = [
        SmallLetters.t,
        SmallLetters.h,
        SmallLetters.e,
        SmallLetters.a,
        SmallLetters.d,
    ]
    tr = [
        SmallLetters.t,
        SmallLetters.r,
    ]
    td = [
        SmallLetters.t,
        SmallLetters.d,
    ]
    th = [
        SmallLetters.t,
        SmallLetters.h,
    ]
    html = [
        SmallLetters.h,
        SmallLetters.t,
        SmallLetters.m,
        SmallLetters.l,
    ]
    body = [
        SmallLetters.b,
        SmallLetters.o,
        SmallLetters.d,
        SmallLetters.y,
    ]
    h1 = [
        SmallLetters.h,
        Digits.One,
    ]
    h2 = [
        SmallLetters.h,
        Digits.Two,
    ]
    h3 = [
        SmallLetters.h,
        Digits.Three,
    ]
    h4 = [
        SmallLetters.h,
        Digits.Four,
    ]
    h5 = [
        SmallLetters.h,
        Digits.Five,
    ]
    h6 = [
        SmallLetters.h,
        Digits.Six,
    ]
    select = [
        SmallLetters.s,
        SmallLetters.e,
        SmallLetters.l,
        SmallLetters.e,
        SmallLetters.c,
        SmallLetters.c,
    ]
    abbr = [
        SmallLetters.a,
        SmallLetters.b,
        SmallLetters.b,
        SmallLetters.r,
    ]

class TagMode(int, Enum):
    StartTag = 0
    EndTag = 0





class GrammarParent(BaseModel):
    start_tag =  Literal[Brackets.LeftAngleBracket]
    end_slash = Optional[Literal[Slashes.ForwardSlash]]
    end_tag =  Literal[Brackets.RightAngleBracket]
    attributes_text: str

class GrammarATag(GrammarParent):    
    chars = Literal[TagsSmallLetterTty.a]
    tag_type: TagsTty.a
    tag_mode: TagMode


class GrammarITag(GrammarParent):
    chars = Literal[TagsSmallLetterTty.i]
    tag_type: TagsTty.i
    tag_mode: TagMode


class GrammarPTag(GrammarParent):
    chars = Literal[TagsSmallLetterTty.p]
    tag_type: TagsTty.p
    tag_mode: TagMode


class GrammarBTag(GrammarParent):
    chars = Literal[TagsSmallLetterTty.b]
    tag_type: TagsTty.b
    tag_mode: TagMode


class GrammarQTag(GrammarParent):
    chars = Literal[TagsSmallLetterTty.q]
    tag_type: TagsTty.q
    tag_mode: TagMode
 


class GrammarUTag(GrammarParent):
    chars = Literal[TagsSmallLetterTty.u]
    tag_type: TagsTty.u
    tag_mode: TagMode


class GrammarStrongTag(GrammarParent):
    chars = Literal[TagsSmallLetterTty.strong]
    tag_type: TagsTty.strong
    tag_mode: TagMode


class GrammarUlTag(GrammarParent):
    chars = Literal[TagsSmallLetterTty.ul]
    tag_type: TagsTty.ul
    tag_mode: TagMode


class GrammarOlTag(GrammarParent):
    chars = Literal[TagsSmallLetterTty.ol]
    tag_type: TagsTty.ol
    tag_mode: TagMode


    
class GrammarLiTag(GrammarParent):
    chars = Literal[TagsSmallLetterTty.li]
    tag_type: TagsTty.li
    tag_mode: TagMode


class GrammarButtonTag(GrammarParent):
    chars = Literal[TagsSmallLetterTty.button]
    tag_type: TagsTty.button
    tag_mode: TagMode


class GrammarInputTag(GrammarParent):
    chars = Literal[TagsSmallLetterTty.input]
    tag_type: TagsTty.input
    tag_mode: TagMode



class GrammarTableTag(GrammarParent):
    chars = Literal[TagsSmallLetterTty.table]
    tag_type: TagsTty.table
    tag_mode: TagMode

     
class GrammarThTag(GrammarParent):
    chars = Literal[TagsSmallLetterTty.th]
    tag_type: TagsTty.th
    tag_mode: TagMode

     
class GrammarTdTag(GrammarParent):
    chars = Literal[TagsSmallLetterTty.td]
    tag_type: TagsTty.td
    tag_mode: TagMode

     
class GrammarTrTag(GrammarParent):
    chars = Literal[TagsSmallLetterTty.tr]
    tag_type: TagsTty.tr
    tag_mode: TagMode

     
class GrammarAbbrTag(GrammarParent):
    chars = Literal[TagsSmallLetterTty.abbr]
    tag_type: TagsTty.abbr
    tag_mode: TagMode

     
class GrammarHtmlTag(GrammarParent):
    chars = Literal[TagsSmallLetterTty.html]
    tag_type: TagsTty.html
    tag_mode: TagMode

     
class GrammarTbodyTag(GrammarParent):
    chars = Literal[TagsSmallLetterTty.tbody]
    tag_type: TagsTty.tbody
    tag_mode: TagMode

     
class GrammarTheadTag(GrammarParent):
    chars = Literal[TagsSmallLetterTty.thead]
    tag_type: TagsTty.thead
    tag_mode: TagMode

     
class GrammarBodyTag(GrammarParent):
    chars = Literal[TagsSmallLetterTty.body]
    tag_type: TagsTty.body
    tag_mode: TagMode

     
class GrammarH1Tag(GrammarParent):
    chars = Literal[TagsSmallLetterTty.h1]
    tag_type: TagsTty.h1
    tag_mode: TagMode

     
class GrammarH2Tag(GrammarParent):
    chars = Literal[TagsSmallLetterTty.h2]
    tag_type: TagsTty.h2
    tag_mode: TagMode

     
class GrammarH3Tag(GrammarParent):
    chars = Literal[TagsSmallLetterTty.h3]
    tag_type: TagsTty.h3
    tag_mode: TagMode

     
class GrammarH4Tag(GrammarParent):
    chars = Literal[TagsSmallLetterTty.h4]
    tag_type: TagsTty.h4
    tag_mode: TagMode

     
class GrammarH5Tag(GrammarParent):
    chars = Literal[TagsSmallLetterTty.h5]
    tag_type: TagsTty.h5
    tag_mode: TagMode

     
class GrammarH6Tag(GrammarParent):
    chars = Literal[TagsSmallLetterTty.h6]
    tag_type: TagsTty.h6
    tag_mode: TagMode

     
class GrammarSelectTag(GrammarParent):
    chars = Literal[TagsSmallLetterTty.select]
    tag_type: TagsTty.select
    tag_mode: TagMode

     