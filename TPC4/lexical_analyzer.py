import ply.lex as lex
import re
import sys

tokens = (
    "COMMENT",
    "SELECT",
    "WHERE",
    "LIMIT",
    "VARIABLE",
    "NUM",
    "STR",
    "PROPERTY",
    "LBRACE",
    "RBRACE",
    "POINT"
)

def t_COMMENT(t):
    r'\#.*'
    return t

def t_SELECT(t):
    r'SELECT|select'
    return t

def t_WHERE(t):
    r'WHERE|where'
    return t

def t_LIMIT(t):
    r'LIMIT|limit'
    return t

def t_VARIABLE(t):
    r'\?\w+'
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STR(t):
    r'\"(?P<CONTENT>.*?)\"(?:@(?P<LAN>\w+))?'
    t.value = re.match(t_STR.__doc__, t.value).groupdict()
    return t

def t_PROPERTY(t):
    r'a|[a-zA-Z]+:[a-zA-Z]+'
    return t

def t_LBRACE(t):
    r'\{'
    return t

def t_RBRACE(t):
    r'\}'
    return t

def t_POINT(t):
    r'\.'
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Ilegal character: {t.value[0]}")
    t.lexer.skip(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python lexical_analyzer.py <query_file_path>")
    else:
        with open(sys.argv[1], 'r') as file:
            lexer = lex.lex()
            lexer.input(file.read())

            while t := lexer.token():
                print(t)
