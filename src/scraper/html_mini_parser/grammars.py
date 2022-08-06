from .lexer_items import *


A_TAG_START_P1 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.a,
    UsualSymbols.SpaceBar
)

A_TAG_START_P2 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.a,
    Brackets.RightAngleBracket
)

A_TAG_END_P1 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.a
)

A_TAG_END_P2 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.a,
    Brackets.RightAngleBracket
)

UL_TAG_START_P1 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.u,
    Letters.SmallLetters.l
)

UL_TAG_START_P2 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.u,
    Letters.SmallLetters.l,
    Brackets.RightAngleBracket
)

UL_TAG_END_P1 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.u,
)

UL_TAG_END_P2 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.u,
    Letters.SmallLetters.l,
    Brackets.RightAngleBracket
)


OL_TAG_START_P1 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.o,
    Letters.SmallLetters.l
)

OL_TAG_START_P2 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.o,
    Letters.SmallLetters.l,
    Brackets.RightAngleBracket
)

OL_TAG_END_P1 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.o,
)

OL_TAG_END_P2 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.o,
    Letters.SmallLetters.l,
    Brackets.RightAngleBracket
)


LI_TAG_START_P1 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.l,
    Letters.SmallLetters.i,
)


LI_TAG_START_P2 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.l,
    Letters.SmallLetters.i,
    Brackets.RightAngleBracket
)

LI_TAG_END_P1 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.l,
)


LI_TAG_END_P2 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.l,
    Letters.SmallLetters.i,
    Brackets.RightAngleBracket
)

P_TAG_START = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.p,
    Brackets.RightAngleBracket,    
)

P_TAG_END = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.p,
)

P_TAG_END_P1 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.p,
    Brackets.RightAngleBracket
)

B_TAG_START = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.b,
    Brackets.RightAngleBracket,    
)

B_TAG_END = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.b,
)

B_TAG_END_P1 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.b,
    Brackets.RightAngleBracket
)

I_TAG_START = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.i,
    Brackets.RightAngleBracket,    
)

I_TAG_END = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.i,
)

I_TAG_END_P1 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.i,
    Brackets.RightAngleBracket
)


H1_TAG_START_P1 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.h,
    Letters.Digits.One,
)

H1_TAG_START_P2 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.h,
    Letters.Digits.One,
    Brackets.RightAngleBracket
)

H1_TAG_END_P1 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.h,
)

H1_TAG_END_P2 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.h,
    Letters.Digits.One,
    Brackets.RightAngleBracket
)

H2_TAG_START_P1 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.h,
    Letters.Digits.Two,
)

H2_TAG_START_P2 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.h,
    Letters.Digits.Two,
    Brackets.RightAngleBracket
)

H2_TAG_END_P1 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.h,
)

H2_TAG_END_P2 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.h,
    Letters.Digits.Two,
    Brackets.RightAngleBracket
)

H3_TAG_START_P1 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.h,
    Letters.Digits.Three,
)

H3_TAG_START_P2 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.h,
    Letters.Digits.Three,
    Brackets.RightAngleBracket
)

H3_TAG_END_P1 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.h,
)

H3_TAG_END_P2 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.h,
    Letters.Digits.Three,
    Brackets.RightAngleBracket
)


H4_TAG_START_P1 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.h,
    Letters.Digits.Four,
)

H4_TAG_START_P2 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.h,
    Letters.Digits.Four,
    Brackets.RightAngleBracket
)

H4_TAG_END_P1 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.h,
)

H4_TAG_END_P2 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.h,
    Letters.Digits.Four,
    Brackets.RightAngleBracket
)

H5_TAG_START_P1 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.h,
    Letters.Digits.Five,
)

H5_TAG_START_P2 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.h,
    Letters.Digits.Five,
    Brackets.RightAngleBracket
)

H5_TAG_END_P1 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.h,
)

H5_TAG_END_P2 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.h,
    Letters.Digits.Five,
    Brackets.RightAngleBracket
)


H6_TAG_START_P1 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.h,
    Letters.Digits.Six,
)

H6_TAG_START_P2 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.h,
    Letters.Digits.Six,
    Brackets.RightAngleBracket
)

H6_TAG_END_P1 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.h,
)

H6_TAG_END_P2 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.h,
    Letters.Digits.Six,
    Brackets.RightAngleBracket
)

BUTTON_TAG_START_P1 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.b,
    Letters.SmallLetters.u,
)

BUTTON_TAG_START_P2 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.b,
    Letters.SmallLetters.u,
    Letters.SmallLetters.t,
    Letters.SmallLetters.t,
    Letters.SmallLetters.o,
    Letters.SmallLetters.n,
    Brackets.RightAngleBracket,
)

BUTTON_TAG_END_P1 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.b,
)

BUTTON_TAG_END_P2 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.b,
    Letters.SmallLetters.u,
    Letters.SmallLetters.t,
    Letters.SmallLetters.t,
    Letters.SmallLetters.o,
    Letters.SmallLetters.n,
    Brackets.RightAngleBracket,
)



BODY_TAG_START_P1 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.b,
    Letters.SmallLetters.o,
)

BODY_TAG_START_P1 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.b,
    Letters.SmallLetters.o,
    Letters.SmallLetters.d,
    Letters.SmallLetters.y,
    Brackets.RightAngleBracket,
)

BODY_TAG_END_P1 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.b,
)

BODY_TAG_END_P2 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.b,
    Letters.SmallLetters.o,
    Letters.SmallLetters.d,
    Letters.SmallLetters.y,
    Brackets.RightAngleBracket,
)


TABLE_TAG_START_P2 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.t,
    Letters.SmallLetters.a,
)

TABLE_TAG_START_P2 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.t,
    Letters.SmallLetters.a,
    Letters.SmallLetters.b,
    Letters.SmallLetters.l,
    Letters.SmallLetters.e,
    Brackets.RightAngleBracket,
)

TABLE_TAG_END_P1 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.t,
)

TABLE_TAG_END_P2 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.t,
    Letters.SmallLetters.a,
    Letters.SmallLetters.b,
    Letters.SmallLetters.l,
    Letters.SmallLetters.e,
    Brackets.RightAngleBracket,
)


TBODY_TAG_START_P1 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.t,
    Letters.SmallLetters.b,
)

TBODY_TAG_START_P1 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.t,
    Letters.SmallLetters.b,
    Letters.SmallLetters.b,
    Letters.SmallLetters.o,
    Letters.SmallLetters.d,
    Letters.SmallLetters.y,
    Brackets.RightAngleBracket,
)

TBODY_TAG_END_P1 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.t,
)

TBODY_TAG_END_P2 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.t,
    Letters.SmallLetters.b,
    Letters.SmallLetters.b,
    Letters.SmallLetters.o,
    Letters.SmallLetters.d,
    Letters.SmallLetters.y,
    Brackets.RightAngleBracket,
)


THEAD_TAG_START_P1 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.t,
    Letters.SmallLetters.h,
)

THEAD_TAG_START_P2 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.t,
    Letters.SmallLetters.h,
    Letters.SmallLetters.e,
    Letters.SmallLetters.a,
    Letters.SmallLetters.d,
    Brackets.RightAngleBracket,
)

THEAD_TAG_END_P2 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.t,
)

THEAD_TAG_END_P2 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.t,
    Letters.SmallLetters.h,
    Letters.SmallLetters.e,
    Letters.SmallLetters.a,
    Letters.SmallLetters.d,
    Brackets.RightAngleBracket,
)


TR_TAG_START_P1 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.t,
    Letters.SmallLetters.r
)

TR_TAG_START_P2 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.t,
    Letters.SmallLetters.r,
    Brackets.RightAngleBracket
)

TR_TAG_END_P1 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.t,
)

TR_TAG_END_P2 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.t,
    Letters.SmallLetters.r,
    Brackets.RightAngleBracket
)

TD_TAG_START_P1 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.t,
    Letters.SmallLetters.d
)

TD_TAG_START_P2 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.t,
    Letters.SmallLetters.d,
    Brackets.RightAngleBracket
)

TD_TAG_END_P1 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.t,
)

TD_TAG_END_P2 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.t,
    Letters.SmallLetters.d,
    Brackets.RightAngleBracket
)

TH_TAG_START_P1 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.t,
    Letters.SmallLetters.h
)

TH_TAG_START_P2 = (
    Brackets.LeftAngleBracket,
    Letters.SmallLetters.t,
    Letters.SmallLetters.h,
    Brackets.RightAngleBracket
)

TH_TAG_END_P1 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.t,
)

TH_TAG_END_P2 = (
    Brackets.LeftAngleBracket,
    Slashes.ForwardSlash,
    Letters.SmallLetters.t,
    Letters.SmallLetters.h,
    Brackets.RightAngleBracket
)