from enum import Enum, auto
from dataclasses import dataclass
from sys import stdin

class TokenType(Enum):
    ON     = auto()
    OFF    = auto()
    EQUALS = auto()
    NUMBER = auto()

@dataclass
class Token:
    type: TokenType
    value: int | None = None

def lexical_analysis(text: str) -> [Token]:
    tokens = list()
    temp_digit_sequence = str()

    i = 0
    while i < len(text):
        if i + 3 < len(text) and text[i:i+3].lower() == "off":
            tokens.append(Token(TokenType.OFF))
            i += 3
        elif i + 2 < len(text) and text[i:i+2].lower() == "on":
            tokens.append(Token(TokenType.ON))
            i += 2
        elif text[i] == "=":
            tokens.append(Token(TokenType.EQUALS))
            i += 1
        elif text[i].isdigit():
            while i < len(text) and text[i].isdigit():
                temp_digit_sequence += text[i]
                i += 1

            tokens.append(Token(TokenType.NUMBER, int(temp_digit_sequence)))
            temp_digit_sequence = ""
        else:
            i += 1

    return tokens

def semantic_analysis(tokens: [Token]):
    sum_digits = 0
    is_on = True

    for token in tokens:
        if token.type == TokenType.ON:
            is_on = True
        elif token.type == TokenType.OFF:
            is_on = False
        elif is_on and token.type == TokenType.NUMBER:
            sum_digits += token.value
        elif token.type == TokenType.EQUALS:
            print(sum_digits)

def main():
    semantic_analysis(lexical_analysis(stdin.read()))

if __name__ == "__main__":
    main()
