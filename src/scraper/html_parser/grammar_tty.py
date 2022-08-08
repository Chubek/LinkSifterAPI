from .lexer_items import Digits, SmallLetters
from typing import List, Union
from enum import Enum
from __future__ import annotations

class TagsAttrListTty(List[str], Enum):
    empty = []
    a = [
        [
            SmallLetters.h,
            SmallLetters.r,
            SmallLetters.e,
            SmallLetters.f
        ],
        [
            SmallLetters.t,
            SmallLetters.a,
            SmallLetters.r,
            SmallLetters.g,
            SmallLetters.e,
            SmallLetters.t
        ],
        [
            SmallLetters.r,
            SmallLetters.e,
            SmallLetters.l
        ]
        [
            SmallLetters.r,
            SmallLetters.e,
            SmallLetters.v
        ]
    ]
    p = []
    b = []
    i = []
    u = []
    q = []
    strong = []
    ul = [
        [
            SmallLetters.c,
            SmallLetters.o,
            SmallLetters.m,
            SmallLetters.p,
            SmallLetters.a,
            SmallLetters.c,
            SmallLetters.t
        ],
        [
            SmallLetters.t,
            SmallLetters.y,
            SmallLetters.p,
            SmallLetters.e
        ],
    ]
    ol = [
        [
            SmallLetters.r,
            SmallLetters.e,
            SmallLetters.v,
            SmallLetters.e,
            SmallLetters.r,
            SmallLetters.s,
            SmallLetters.e,
            SmallLetters.d
        ],
        [
            SmallLetters.s,
            SmallLetters.t,
            SmallLetters.a,
            SmallLetters.r,
            SmallLetters.t
        ],
        [
            SmallLetters.t,
            SmallLetters.y,
            SmallLetters.p,
            SmallLetters.e
        ]
    ]
    li = [
        [
            SmallLetters.v,
            SmallLetters.a,
            SmallLetters.l,
            SmallLetters.u,
            SmallLetters.e
        ],
        [
            SmallLetters.t,
            SmallLetters.y,
            SmallLetters.p,
            SmallLetters.e
        ],
    ]
    button = [
        [
            SmallLetters.a,
            SmallLetters.u,
            SmallLetters.t,
            SmallLetters.o,
            SmallLetters.f,
            SmallLetters.o,
            SmallLetters.c,
            SmallLetters.u,
            SmallLetters.s
        ],
        [
            SmallLetters.a,
            SmallLetters.u,
            SmallLetters.t,
            SmallLetters.o,
            SmallLetters.c,
            SmallLetters.o,
            SmallLetters.m,
            SmallLetters.p,
            SmallLetters.l,
            SmallLetters.e,
            SmallLetters.t,
            SmallLetters.e
        ],
        [
            SmallLetters.d,
            SmallLetters.i,
            SmallLetters.s,
            SmallLetters.a,
            SmallLetters.b,
            SmallLetters.l,
            SmallLetters.e,
            SmallLetters.d
        ],
        [
            SmallLetters.f,
            SmallLetters.o,
            SmallLetters.r,
            SmallLetters.m
        ],
        [
            SmallLetters.f,
            SmallLetters.o,
            SmallLetters.r,
            SmallLetters.m,
            SmallLetters.e,
            SmallLetters.n,
            SmallLetters.c,
            SmallLetters.t,
            SmallLetters.y,
            SmallLetters.p,
            SmallLetters.e
        ],
        [
            SmallLetters.f,
            SmallLetters.o,
            SmallLetters.r,
            SmallLetters.m,
            SmallLetters.m,
            SmallLetters.e,
            SmallLetters.t,
            SmallLetters.h,
            SmallLetters.o,
            SmallLetters.d
        ],
        [
            SmallLetters.f,
            SmallLetters.o,
            SmallLetters.r,
            SmallLetters.m,
            SmallLetters.n,
            SmallLetters.o,
            SmallLetters.v,
            SmallLetters.a,
            SmallLetters.l,
            SmallLetters.i,
            SmallLetters.d,
            SmallLetters.a,
            SmallLetters.t,
            SmallLetters.e
        ],
        [
            SmallLetters.f,
            SmallLetters.o,
            SmallLetters.r,
            SmallLetters.m,
            SmallLetters.t,
            SmallLetters.a,
            SmallLetters.r,
            SmallLetters.g,
            SmallLetters.e,
            SmallLetters.t
        ],
        [
            SmallLetters.n,
            SmallLetters.a,
            SmallLetters.m,
            SmallLetters.e
        ],
        [
            SmallLetters.t,
            SmallLetters.y,
            SmallLetters.p,
            SmallLetters.e
        ],
        [
            SmallLetters.v,
            SmallLetters.a,
            SmallLetters.l,
            SmallLetters.u,
            SmallLetters.e
        ],
    ]
    input = [
        [
            SmallLetters.a,
            SmallLetters.c,
            SmallLetters.c,
            SmallLetters.e,
            SmallLetters.p,
            SmallLetters.t
        ],
        [
            SmallLetters.a,
            SmallLetters.l,
            SmallLetters.l
        ],
        [
            SmallLetters.a,
            SmallLetters.u,
            SmallLetters.t,
            SmallLetters.o,
            SmallLetters.c,
            SmallLetters.o,
            SmallLetters.m,
            SmallLetters.p,
            SmallLetters.l,
            SmallLetters.e,
            SmallLetters.t,
            SmallLetters.e
        ],
        [
            SmallLetters.c,
            SmallLetters.a,
            SmallLetters.p,
            SmallLetters.t,
            SmallLetters.u,
            SmallLetters.r,
            SmallLetters.e
        ],
        [
            SmallLetters.c,
            SmallLetters.h,
            SmallLetters.e,
            SmallLetters.c,
            SmallLetters.k,
            SmallLetters.e,
            SmallLetters.d
        ],
        [
            SmallLetters.d,
            SmallLetters.i,
            SmallLetters.r,
            SmallLetters.n,
            SmallLetters.a,
            SmallLetters.m,
            SmallLetters.e
        ],
        [
            SmallLetters.d,
            SmallLetters.i,
            SmallLetters.s,
            SmallLetters.a,
            SmallLetters.b,
            SmallLetters.l,
            SmallLetters.e,
            SmallLetters.d
        ],
        [
            SmallLetters.f,
            SmallLetters.o,
            SmallLetters.r,
            SmallLetters.m
        ],
        [
            SmallLetters.f,
            SmallLetters.o,
            SmallLetters.r,
            SmallLetters.m,
            SmallLetters.a,
            SmallLetters.c,
            SmallLetters.t,
            SmallLetters.i,
            SmallLetters.o,
            SmallLetters.n
        ],
        [
            SmallLetters.f,
            SmallLetters.o,
            SmallLetters.r,
            SmallLetters.m,
            SmallLetters.e,
            SmallLetters.n,
            SmallLetters.c,
            SmallLetters.t,
            SmallLetters.y,
            SmallLetters.p,
            SmallLetters.e
        ],
        [
            SmallLetters.f,
            SmallLetters.o,
            SmallLetters.r,
            SmallLetters.m,
            SmallLetters.m,
            SmallLetters.e,
            SmallLetters.t,
            SmallLetters.h,
            SmallLetters.o,
            SmallLetters.d
        ],
        [
            SmallLetters.f,
            SmallLetters.o,
            SmallLetters.r,
            SmallLetters.m,
            SmallLetters.n,
            SmallLetters.o,
            SmallLetters.v,
            SmallLetters.a,
            SmallLetters.l,
            SmallLetters.i,
            SmallLetters.d,
            SmallLetters.a,
            SmallLetters.t,
            SmallLetters.e
        ],
        [
            SmallLetters.f,
            SmallLetters.o,
            SmallLetters.r,
            SmallLetters.m,
            SmallLetters.t,
            SmallLetters.a,
            SmallLetters.r,
            SmallLetters.g,
            SmallLetters.e,
            SmallLetters.t
        ],
        [
            SmallLetters.h,
            SmallLetters.e,
            SmallLetters.i,
            SmallLetters.g,
            SmallLetters.h,
            SmallLetters.t
        ],
        [
            SmallLetters.l,
            SmallLetters.i,
            SmallLetters.s,
            SmallLetters.t
        ],
        [
            SmallLetters.m,
            SmallLetters.a,
            SmallLetters.x
        ],
        [
            SmallLetters.m,
            SmallLetters.a,
            SmallLetters.x,
            SmallLetters.l,
            SmallLetters.e,
            SmallLetters.n,
            SmallLetters.g,
            SmallLetters.t,
            SmallLetters.h
        ],
        [
            SmallLetters.m,
            SmallLetters.i,
            SmallLetters.n
        ],
        [
            SmallLetters.m,
            SmallLetters.i,
            SmallLetters.n,
            SmallLetters.l,
            SmallLetters.e,
            SmallLetters.n,
            SmallLetters.g,
            SmallLetters.t,
            SmallLetters.h
        ],
        [
            SmallLetters.m,
            SmallLetters.u,
            SmallLetters.l,
            SmallLetters.t,
            SmallLetters.i,
            SmallLetters.p,
            SmallLetters.l,
            SmallLetters.e
        ],
        [
            SmallLetters.p,
            SmallLetters.a,
            SmallLetters.t,
            SmallLetters.t,
            SmallLetters.e,
            SmallLetters.r,
            SmallLetters.n
        ],
        [
            SmallLetters.p,
            SmallLetters.l,
            SmallLetters.a,
            SmallLetters.c,
            SmallLetters.e,
            SmallLetters.h,
            SmallLetters.o,
            SmallLetters.l,
            SmallLetters.d,
            SmallLetters.e,
            SmallLetters.r
        ],
        [
            SmallLetters.r,
            SmallLetters.e,
            SmallLetters.a,
            SmallLetters.d,
            SmallLetters.o,
            SmallLetters.n,
            SmallLetters.l,
            SmallLetters.y
        ],
        [
            SmallLetters.r,
            SmallLetters.e,
            SmallLetters.q,
            SmallLetters.u,
            SmallLetters.i,
            SmallLetters.r,
            SmallLetters.e,
            SmallLetters.d
        ],
        [
            SmallLetters.s,
            SmallLetters.i,
            SmallLetters.z,
            SmallLetters.e
        ],
        [
            SmallLetters.s,
            SmallLetters.r,
            SmallLetters.c
        ],
        [
            SmallLetters.t,
            SmallLetters.y,
            SmallLetters.p,
            SmallLetters.e
        ],
        [
            SmallLetters.v,
            SmallLetters.a,
            SmallLetters.l,
            SmallLetters.u,
            SmallLetters.e
        ],
        [
            SmallLetters.w,
            SmallLetters.i,
            SmallLetters.d,
            SmallLetters.t,
            SmallLetters.h
        ],
    ]
    table = [
        [
            SmallLetters.b,
            SmallLetters.o,
            SmallLetters.r,
            SmallLetters.d,
            SmallLetters.e,
            SmallLetters.r
        ],
        [
            SmallLetters.c,
            SmallLetters.e,
            SmallLetters.l,
            SmallLetters.l,
            SmallLetters.s,
            SmallLetters.p,
            SmallLetters.a,
            SmallLetters.c,
            SmallLetters.i,
            SmallLetters.n,
            SmallLetters.g
        ],
        [
            SmallLetters.h,
            SmallLetters.e,
            SmallLetters.i,
            SmallLetters.g,
            SmallLetters.h,
            SmallLetters.t
        ],
        [
            SmallLetters.w,
            SmallLetters.i,
            SmallLetters.d,
            SmallLetters.t,
            SmallLetters.h
        ],
        [
            SmallLetters.r,
            SmallLetters.u,
            SmallLetters.l,
            SmallLetters.e,
            SmallLetters.s
        ],
        [
            SmallLetters.f,
            SmallLetters.r,
            SmallLetters.a,
            SmallLetters.m,
            SmallLetters.e
        ],
        [
            SmallLetters.s,
            SmallLetters.u,
            SmallLetters.m,
            SmallLetters.m,
            SmallLetters.a,
            SmallLetters.r,
            SmallLetters.y
        ],
    ]
    tbody = [
        [
            SmallLetters.a,
            SmallLetters.l,
            SmallLetters.i,
            SmallLetters.g,
            SmallLetters.n
        ],
        [
            SmallLetters.b,
            SmallLetters.g,
            SmallLetters.c,
            SmallLetters.o,
            SmallLetters.l,
            SmallLetters.o,
            SmallLetters.r
        ],
        [
            SmallLetters.c,
            SmallLetters.h,
            SmallLetters.a,
            SmallLetters.r
        ],
        [
            SmallLetters.c,
            SmallLetters.h,
            SmallLetters.a,
            SmallLetters.r,
            SmallLetters.o,
            SmallLetters.f,
            SmallLetters.f
        ],
        [
            SmallLetters.v,
            SmallLetters.a,
            SmallLetters.l,
            SmallLetters.i,
            SmallLetters.g,
            SmallLetters.n
        ],

    ]
    thead = [
        [
            SmallLetters.a,
            SmallLetters.l,
            SmallLetters.i,
            SmallLetters.g,
            SmallLetters.n
        ],
        [
            SmallLetters.b,
            SmallLetters.g,
            SmallLetters.c,
            SmallLetters.o,
            SmallLetters.l,
            SmallLetters.o,
            SmallLetters.r
        ],
        [
            SmallLetters.c,
            SmallLetters.h,
            SmallLetters.a,
            SmallLetters.r
        ],
        [
            SmallLetters.c,
            SmallLetters.h,
            SmallLetters.a,
            SmallLetters.r,
            SmallLetters.o,
            SmallLetters.f,
            SmallLetters.f
        ],
        [
            SmallLetters.v,
            SmallLetters.a,
            SmallLetters.l,
            SmallLetters.i,
            SmallLetters.g,
            SmallLetters.n
        ],
    ]
    tr = [
        [
            SmallLetters.a,
            SmallLetters.l,
            SmallLetters.i,
            SmallLetters.g,
            SmallLetters.n
        ],
        [
            SmallLetters.v,
            SmallLetters.a,
            SmallLetters.l,
            SmallLetters.i,
            SmallLetters.g,
            SmallLetters.n
        ]
    ]
    td = [
        [
            SmallLetters.c,
            SmallLetters.o,
            SmallLetters.l,
            SmallLetters.s,
            SmallLetters.p,
            SmallLetters.a,
            SmallLetters.n
        ],
        [
            SmallLetters.r,
            SmallLetters.o,
            SmallLetters.w,
            SmallLetters.s,
            SmallLetters.p,
            SmallLetters.a,
            SmallLetters.n
        ],
        [
            SmallLetters.a,
            SmallLetters.l,
            SmallLetters.i,
            SmallLetters.g,
            SmallLetters.n
        ],
        [
            SmallLetters.v,
            SmallLetters.a,
            SmallLetters.l,
            SmallLetters.i,
            SmallLetters.g,
            SmallLetters.n
        ]
    ]
    th = []
    html = [
        [
            SmallLetters.m,
            SmallLetters.a,
            SmallLetters.n,
            SmallLetters.i,
            SmallLetters.f,
            SmallLetters.e,
            SmallLetters.s,
            SmallLetters.t
        ],
        [
            SmallLetters.v,
            SmallLetters.e,
            SmallLetters.r,
            SmallLetters.s,
            SmallLetters.i,
            SmallLetters.o,
            SmallLetters.n
        ],
        [
            SmallLetters.x,
            SmallLetters.m,
            SmallLetters.l,
            SmallLetters.n,
            SmallLetters.s
        ]
    ]
    body = [
        [
            SmallLetters.b,
            SmallLetters.g,
            SmallLetters.c,
            SmallLetters.o,
            SmallLetters.l,
            SmallLetters.o,
            SmallLetters.r
        ],
        [
            SmallLetters.b,
            SmallLetters.a,
            SmallLetters.c,
            SmallLetters.k,
            SmallLetters.g,
            SmallLetters.r,
            SmallLetters.o,
            SmallLetters.u,
            SmallLetters.n,
            SmallLetters.d
        ],
        [
            SmallLetters.t,
            SmallLetters.e,
            SmallLetters.x,
            SmallLetters.t
        ],
        [
            SmallLetters.l,
            SmallLetters.i,
            SmallLetters.n,
            SmallLetters.k
        ],
        [
            SmallLetters.a,
            SmallLetters.l,
            SmallLetters.i,
            SmallLetters.n,
            SmallLetters.k
        ],
        [
            SmallLetters.v,
            SmallLetters.l,
            SmallLetters.i,
            SmallLetters.n,
            SmallLetters.k
        ]
    ]
    h1 = []
    h2 = []
    h3 = []
    h4 = []
    h5 = []
    h6 = []
    select = [
        [
            SmallLetters.a,
            SmallLetters.u,
            SmallLetters.t,
            SmallLetters.o,
            SmallLetters.c,
            SmallLetters.o,
            SmallLetters.m,
            SmallLetters.p,
            SmallLetters.l,
            SmallLetters.e,
            SmallLetters.t,
            SmallLetters.e
        ],
        [
            SmallLetters.a,
            SmallLetters.u,
            SmallLetters.t,
            SmallLetters.o,
            SmallLetters.f,
            SmallLetters.o,
            SmallLetters.c,
            SmallLetters.u,
            SmallLetters.s
        ],
        [
            SmallLetters.d,
            SmallLetters.i,
            SmallLetters.s,
            SmallLetters.a,
            SmallLetters.b,
            SmallLetters.l,
            SmallLetters.e,
            SmallLetters.d
        ],
        [
            SmallLetters.f,
            SmallLetters.o,
            SmallLetters.r,
            SmallLetters.m
        ],
        [
            SmallLetters.m,
            SmallLetters.u,
            SmallLetters.l,
            SmallLetters.t,
            SmallLetters.i,
            SmallLetters.p,
            SmallLetters.l,
            SmallLetters.e
        ],
        [
            SmallLetters.n,
            SmallLetters.a,
            SmallLetters.m,
            SmallLetters.e
        ],
        [
            SmallLetters.r,
            SmallLetters.e,
            SmallLetters.q,
            SmallLetters.u,
            SmallLetters.i,
            SmallLetters.r,
            SmallLetters.e,
            SmallLetters.d
        ],
        [
            SmallLetters.s,
            SmallLetters.i,
            SmallLetters.z,
            SmallLetters.e
        ]
    ]
    abbr = [
        SmallLetters.a,
        SmallLetters.b,
        SmallLetters.b,
        SmallLetters.r,
    ]
    img = [
        [
            SmallLetters.s,
            SmallLetters.r,
            SmallLetters.c
        ],
        [
            SmallLetters.a,
            SmallLetters.l,
            SmallLetters.t
        ],
        [
            SmallLetters.b,
            SmallLetters.o,
            SmallLetters.r,
            SmallLetters.d,
            SmallLetters.e,
            SmallLetters.r
        ],
        [
            SmallLetters.w,
            SmallLetters.i,
            SmallLetters.d,
            SmallLetters.t,
            SmallLetters.h
        ],
        [
            SmallLetters.h,
            SmallLetters.e,
            SmallLetters.i,
            SmallLetters.g,
            SmallLetters.h,
            SmallLetters.t
        ],
        [
            SmallLetters.h,
            SmallLetters.s,
            SmallLetters.p,
            SmallLetters.a,
            SmallLetters.c,
            SmallLetters.e
        ]
        [
            SmallLetters.v,
            SmallLetters.s,
            SmallLetters.p,
            SmallLetters.a,
            SmallLetters.c,
            SmallLetters.e
        ]
        [
            SmallLetters.u,
            SmallLetters.s,
            SmallLetters.e,
            SmallLetters.r,
            SmallLetters.m,
            SmallLetters.a,
            SmallLetters.p
        ]
    ]
    title = []
    main = []
    options = [
        [
            SmallLetters.d,
            SmallLetters.i,
            SmallLetters.s,
            SmallLetters.a,
            SmallLetters.b,
            SmallLetters.l,
            SmallLetters.e,
            SmallLetters.d
        ],
        [
            SmallLetters.l,
            SmallLetters.a,
            SmallLetters.b,
            SmallLetters.e,
            SmallLetters.l
        ],
        [
            SmallLetters.s,
            SmallLetters.e,
            SmallLetters.l,
            SmallLetters.e,
            SmallLetters.c,
            SmallLetters.t,
            SmallLetters.e,
            SmallLetters.d
        ],
        [
            SmallLetters.v,
            SmallLetters.a,
            SmallLetters.l,
            SmallLetters.u,
            SmallLetters.e
        ]
    ]
    label = [
        [
            SmallLetters.f,
            SmallLetters.o,
            SmallLetters.r
        ]
    ]


class TagsTty(str, Enum):
    null = "null"
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
    img = "img"
    title = "title"
    main = "main"
    span = "span"
    options = "options"
    label = "label"

    @classmethod
    def new(cls, s: Union[str, List[SmallLetters]]) -> TagsTty:
        match s:
            case 'a' | [SmallLetters.a]:
                return TagsTty.a
            case 'p' | [SmallLetters.p]:
                return TagsTty.p
            case 'b' | [SmallLetters.b]:
                return TagsTty.b
            case 'i' | [SmallLetters.i]:
                return TagsTty.i
            case 'u' | [SmallLetters.u]:
                return TagsTty.u
            case 'q' | [SmallLetters.q]:
                return TagsTty.q
            case 'strong' | [
        SmallLetters.s,
        SmallLetters.t,
        SmallLetters.r,
        SmallLetters.o,
        SmallLetters.n,
        SmallLetters.g,
    ]:
                return TagsTty.strong
            case 'ul' | [
        SmallLetters.u,
        SmallLetters.l,
    ]:
                return TagsTty.ul
            case 'ol' | [
        SmallLetters.o,
        SmallLetters.l,
    ]:
                return TagsTty.ol
            case 'li' | [
        SmallLetters.l,
        SmallLetters.i,
    ]:
                return TagsTty.li
            case 'button' | [
        SmallLetters.b,
        SmallLetters.u,
        SmallLetters.t,
        SmallLetters.t,
        SmallLetters.o,
        SmallLetters.n,
    ]:
                return TagsTty.button
            case 'input' | [
        SmallLetters.i,
        SmallLetters.n,
        SmallLetters.p,
        SmallLetters.u,
        SmallLetters.t,
    ]:
                return TagsTty.input
            case 'table' | [
        SmallLetters.t,
        SmallLetters.a,
        SmallLetters.b,
        SmallLetters.l,
        SmallLetters.e,
    ] :
                return TagsTty.table
            case 'tbody' | [
        SmallLetters.t,
        SmallLetters.b,
        SmallLetters.o,
        SmallLetters.d,
        SmallLetters.y,
    ]:
                return TagsTty.tbody
            case 'thead' |  [
        SmallLetters.t,
        SmallLetters.h,
        SmallLetters.e,
        SmallLetters.a,
        SmallLetters.d,
    ]:
                return TagsTty.thead
            case 'tr' | [
        SmallLetters.t,
        SmallLetters.r,
    ]:
                return TagsTty.tr
            case 'td' | [
        SmallLetters.t,
        SmallLetters.d,
    ]:
                return TagsTty.td
            case 'th' | [
        SmallLetters.t,
        SmallLetters.h,
    ]:
                return TagsTty.th
            case 'html' | [
        SmallLetters.h,
        SmallLetters.t,
        SmallLetters.m,
        SmallLetters.l,
    ]:
                return TagsTty.html
            case 'body':
                return TagsTty.body
            case 'h1':
                return TagsTty.h1
            case 'h2':
                return TagsTty.h3
            case 'h4':
                return TagsTty.h4
            case 'h5':
                return TagsTty.h5
            case 'h6':
                return TagsTty.h6
            case 'select':
                return TagsTty.select
            case 'abbr':
                return TagsTty.abbr
            case 'select':
                return TagsTty.select
            case 'img':
                return TagsTty.img
            case 'title':
                return TagsTty.title
            case 'main':
                return TagsTty.main
            case 'span':
                return TagsTty.span
            case 'options':
                return TagsTty.options
            case 'label':
                return TagsTty.label
            case _:
                return TagsTty.null


class TagsSmallLetterTty(List[SmallLetters], Enum):
    empty = []
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
    img = [
        SmallLetters.i,
        SmallLetters.m,
        SmallLetters.g
    ]
    title = [
        SmallLetters.t,
        SmallLetters.i,
        SmallLetters.t,
        SmallLetters.l,
        SmallLetters.e
    ]
    main = [
        SmallLetters.m,
        SmallLetters.a,
        SmallLetters.i,
        SmallLetters.n,
    ]
    span = [
        SmallLetters.s,
        SmallLetters.p,
        SmallLetters.a,
        SmallLetters.n,
    ]
    options = [
        SmallLetters.o,
        SmallLetters.p,
        SmallLetters.t,
        SmallLetters.i,
        SmallLetters.o,
        SmallLetters.n
    ]
    label = [
        SmallLetters.l,
        SmallLetters.a,
        SmallLetters.b,
        SmallLetters.e,
        SmallLetters.l,
    ]


class TagMode(int, Enum):
    StartTag = 0
    EndTag = 0
