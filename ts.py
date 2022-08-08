tt = ["""

class TagsAttrListTty(List[str], Enum):
    empty = []
    a = [
        'href',
        'target',
        'rel'
        'rev'
    ]
    p = []
    b = []
    i = []
    u = []
    q = []
    strong = []
    ul = [
        'compact',
        'type',        
    ]
    ol = [
        'reversed',
        'start',
        'type'
    ]
    li = [
        'value',
        'type',
    ]
    button = [
        'autofocus',
        'autocomplete',
        'disabled',
        'form',
        'formenctype',
        'formmethod',
        'formnovalidate',
        'formtarget',
        'name',
        'type',
        'value',
    ]
    input = [
        'accept',
        'all',
        'autocomplete',
        'capture',
        'checked',
        'dirname',
        'disabled',
        'form',
        'formaction',
        'formenctype',
        'formmethod',
        'formnovalidate',
        'formtarget',
        'height',
        'list',
        'max',
        'maxlength',
        'min',
        'minlength',
        'multiple',
        'pattern',
        'placeholder',
        'readonly',
        'required',
        'size',
        'src',
        'type',
        'value',
        'width',
    ]
    table = [
        'border',
        'cellspacing',
        'height',
        'width',
        'rules',
        'frame',
        'summary',
    ]
    tbody = [
        'align',
        'bgcolor',
        'char',
        'charoff',
        'valign',
        
    ]
    thead = [
        'align',
        'bgcolor',
        'char',
        'charoff',
        'valign',
    ]
    tr = [
        'align',
        'valign'
    ]
    td = [
        'colspan',
        'rowspan',
        'align',
        'valign'
    ]
    th = []
    html = [
        'manifest',
        'version',
        'xmlns'
    ]
    body = [
        'bgcolor',
        'background',
        'text',
        'link',
        'alink',
        'vlink'
    ]
    h1 = []
    h2 = []
    h3 = []
    h4 = []
    h5 = []
    h6 = []
    select = [
        'autocomplete',
        'autofocus',
        'disabled',
        'form',
        'multiple',
        'name',
        'required',
        'size'
    ]
    abbr = [
        SmallLetters.a,
        SmallLetters.b,
        SmallLetters.b,
        SmallLetters.r,
    ]
    img = [
        'src',
        'alt',
        'border',
        'width',
        'height',
        'hspace'
        'vspace'
        'usermap'
    ]
    title = []
    main = []
    options = [
        'disabled',
        'label',
        'selected',
        'value'
    ]
    label = [
        'for'
    ]


"""]

import re

ptt = re.compile(r"\'[a-z]\'")

def rep(x):
    group = x.group(0)
    group_rep = group.replace("'", "")

    group_list = list(group_rep)

    lst = ",\n".join([
        f"SmallLetters.{m}"
        for m in
        group_list
    ])

    tt[0] = tt[0].replace(group, f"[\n{lst}\n]")





re.sub(r"\'[a-z]+\'", rep, tt[0])


print(tt[0], file=open("ffs.txt", "w"))