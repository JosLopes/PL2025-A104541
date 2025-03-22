import ply.lex as lex

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'TERMINATOR'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_TERMINATOR = r'\n'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = None
        self.next_token()

    def next_token(self):
        self.current_token = self.lexer.token()
        return self.current_token # to debug

    def parse(self):
        result = self.exp()
        if self.current_token.type != 'TERMINATOR':
            raise SyntaxError("Unexpected token at the end of expression")
        return result

    def exp(self):
        result = self.term()

        if self.current_token.type == 'PLUS':
            self.next_token()
            return result + self.exp()
        elif self.current_token.type == 'MINUS':
            self.next_token()
            return result - self.exp()
        elif self.current_token.type in ['RPAREN', 'TERMINATOR']:
            return result
        else:
            raise SyntaxError(f"Unexpected token: {self.current_token}")

    def term(self):
        result = self.factor()

        if self.current_token.type == 'TIMES':
            self.next_token()
            return result * self.term()
        elif self.current_token.type == 'DIVIDE':
            self.next_token()
            return result / self.term()
        elif self.current_token.type in ['PLUS', 'MINUS', 'RPAREN', 'TERMINATOR']:
            return result
        else:
            raise SyntaxError(f"Unexpected token: {self.current_token}")

    def factor(self):
        if self.current_token.type == 'NUMBER':
            result = self.current_token.value
            self.next_token()
            return result
        elif self.current_token.type == 'LPAREN':
            self.next_token()
            result = self.exp()

            if self.current_token.type != 'RPAREN':
                raise SyntaxError("Expected ')'")

            self.next_token()
            return result
        else:
            raise SyntaxError(f"Unexpected token: {self.current_token}")

expressions = [
    "16\n",
    "(1)\n",
    "2+ 3\n",
    "67 - (2 +3*4)\n",
    "(9   -2)* (13 - 4 )\n"
]

for expr in expressions:
    lexer.input(expr)
    parser = Parser(lexer)
    try:
        result = parser.parse()
        print(f"Result of '{expr}' is {result}")
    except SyntaxError as e:
        print(f"Syntax error in expression '{expr}': {e}")
