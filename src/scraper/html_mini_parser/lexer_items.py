from pydantic import BaseModel
from typing import Literal

class Brackets(BaseModel):
    LeftAngleBracket = Literal['<']
    RightAngleBracket = Literal['>']
    LeftParanBracket = Literal['(']
    RightParanleBracket = Literal[')']
    LeftSquareBracket = Literal['[']
    RightSquareleBracket = Literal[']']
    LeftCurlyBracket = Literal['{']
    RightCurlyleBracket = Literal['}']

class Slashes(BaseModel):
    ForwardSlash = Literal['/']
    BackwardSlash = Literal['\\']

class SpecialSymbolsCode(BaseModel):
    AcuteAccent = Literal['&#180;']
    Ampersand   = Literal['&#38;']
    CentSign = Literal['&#162;']
    Copyright = Literal['&#169;']
    Dagger = Literal['&#180;']
    DegreeSign = Literal['&#247;']
    DivisionSign = Literal['&#180;']
    Euro = Literal['&#8363;']
    FractionOneHalf	 = Literal['&#189;']
    FractionOneFourth = Literal['&#188;']
    FractionThreeFouths	 = Literal['&#190;']
    GreaterThan = Literal['&#62;']
    LeftAngleQuote = Literal['&#171;']
    LessThan = Literal['&#60;']
    Multiply = Literal['&#215;']
    PlusMinus = Literal['&#177;']
    LeftQuotation = Literal['&#8220;']
    RightQuotation = Literal['&#8221;']
    RightAngleQuote = Literal['&#185;']
    SuperScriptOne = Literal['&#187;']
    Trademark = Literal['&#8482;']




