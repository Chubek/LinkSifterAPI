from enum import Enum
from pydantic import BaseModel
from typing import Literal


class Brackets(str, Enum):
    LeftAngleBracket = '<'
    RightAngleBracket = '>'
    LeftParanBracket = '('
    RightParanleBracket = ')'
    LeftSquareBracket = '['
    RightSquareleBracket = ''
    LeftCurlyBracket = '{'
    RightCurlyleBracket = '}'


class Slashes(str, Enum):
    ForwardSlash = '/'
    BackwardSlash = '\\'


class SpecialCharacters(str, Enum):
    AcuteAccent = '&#180;'
    Ampersand = '&#38;'
    CentSign = '&#162;'
    Copyright = '&#169;'
    Dagger = '&#180;'
    DegreeSign = '&#247;'
    DivisionSign = '&#180;'
    Euro = '&#8363;'
    FractionOneHalf = '&#189;'
    FractionOneFourth = '&#188;'
    FractionThreeFouths = '&#190;'
    GreaterThan = '&#62;'
    LeftAngleQuote = '&#171;'
    LessThan = '&#60;'
    Multiply = '&#215;'
    PlusMinus = '&#177;'
    LeftQuotation = '&#8220;'
    RightQuotation = '&#8221;'
    RightAngleQuote = '&#185;'
    SuperScriptOne = '&#187;'
    Trademark = '&#8482;'


class Symbols(str, Enum):
    Asterisk = '*'
    SingleQuote = "'"
    DoubleQuote = '"'
    AtSign = '@'
    PercentSign = '%'
    DollarSign = '$'
    Caret = '^'
    Dash = '-'
    Pipe = '|'
    UnderLine = '_'
    Ampersand = '&'
    Pound = '#'
    Excl = '!'
    EqualSign = '='
    Colon = ':'
    SemiColon = ';'
    PlusSign = '+'
    SpaceBar = ' '


class CapitalLetters(str, Enum):
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


class SmallLetters(str, Enum):
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


class Digits(str, Enum):
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
