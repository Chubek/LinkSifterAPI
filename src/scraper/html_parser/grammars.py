from typing import List, Literal, Optional, Tuple
from .lexer_items import *
from enum import Enum
from pydantic import BaseModel
from .grammar_tty import *


class GrammarParent(BaseModel):
    start_tag = Literal[Brackets.LeftAngleBracket]
    end_slash = Optional[Literal[Slashes.ForwardSlash]]
    end_tag = Literal[Brackets.RightAngleBracket]
    chars = TagsSmallLetterTty = TagsSmallLetterTty.empty
    tag_type: TagsTty = TagsTty.null
    tag_mode: TagMode
    attribute_keys: Optional[List[str]]

    chars_buffer: List[SmallLetters]


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
