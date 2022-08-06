from enum import Enum
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


class UsualSymbols(BaseModel):
    Asterisk = Literal['*']
    SingleQuote = Literal["'"]
    DoubleQuote = Literal['"']
    AtSign = Literal['@']
    PercentSign = Literal['%']
    DollarSign = Literal['$']
    Caret = Literal['^']
    Dash = Literal['-']
    Pipe = Literal['|']    
    UnderLine = Literal['_']
    Ampersand = Literal['&']
    Pound = Literal['#']
    Excl = Literal['!']
    EqualSign = Literal['=']
    Colon = Literal[':']
    SemiColon = Literal[';']
    PlusSign = Literal['+']
    SpaceBar = Literal[' ']

class CapitalLettersEnum(str, Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    H = "H"
    I = "I"
    J = "J"
    K = "K"
    L = "L"
    M = "M"
    N = "N"
    O = "O"
    P = "P"
    Q = "Q"
    R = "R"
    S = "S"
    T = "T"
    U = "U"
    V = "V"
    W = "W"
    X = "X"
    Y = "Y"
    Z = "Z"

class SmallLettersEnum(str, Enum):
    a = "a"
    b = "b"
    c = "c"
    d = "d"
    e = "e"
    f = "f"
    g = "g"
    h = "h"
    i = "i"
    j = "j"
    k = "k"
    l = "l"
    m = "m"
    n = "n"
    o = "o"
    p = "p"
    q = "q"
    r = "r"
    s = "s"
    t = "t"
    u = "u"
    v = "v"
    w = "w"
    x = "x"
    y = "y"
    z = "z"


class DigitsEnum(str, Enum):
    One = "1"
    Two = "2"
    Three = "3"
    Four = "4"
    Five = "5"
    Six = "6"
    Seven = "7"
    Eigth = "8"
    Nine = "9"
    Zero = "0"

class Letters(BaseModel):
    CapitalLetters = CapitalLettersEnum
    SmallLetters = SmallLettersEnum
    Digits = DigitsEnum



