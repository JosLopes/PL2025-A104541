# PL2025 - TPC6
## Descrição do problema

Este documento apresenta a documentação relativa ao sexto trabalho de casa
proposto pela cadeira de processamento de linguagens. Foi pedido um *parser*
LL(1) recursivo descendente, escrito em python, que reconheça expressões
aritméticas e calcule o respetivo valor.

## Metodologia

Para construir o *parser* desenvolvi, primeiramente, uma gramática que
acomodasse expressões aritméticas simples, a qual apresento de seguida:

```
    T = {
        'NUMBER',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'LPAREN',
        'RPAREN',
        'TERMINATOR'
    }

    P = {
        parse -> exp 'TERMINATOR'

        exp -> term exp2

        exp2 -> 'PLUS' exp
        exp2 -> 'MINUS' exp
        exp2 -> ε

        term -> factor term2

        term2 -> 'TIMES' term
        term2 -> 'DIVIDE' term
        term2 -> ε

        factor -> 'LPAREN' exp 'RPAREN'
        factor -> 'NUMBER'
    }
```

Bastou, por fim, mapear esta gramática para código, o qual está disponível para
consulta no ficheiro [syntactic_analyzer.py](syntactic_analyzer.py). Além do
analisador sintático, foi também necessário construir um analisador léxico, de
modo a extrair os *tokens* de cada expressão. A sua implementação foi realizada com
recurso à biblioteca ```ply.lex``` e é bastante simples, pelo que não necessita
de nenhuma documentação adicional.

## Resultados e Conclusão

O programa pode ser executado da seguinte forma:

```
$ python3 syntactic_analyzer.py
```

Este programa foi verificado para as expressões exemplo demonstradas abaixo,
pelo que o considerei correto.

```
    "16\n",
    "(1)\n",
    "2+ 3\n",
    "67 - (2 +3*4)\n",
    "(9   -2)* (13 - 4 )\n"
```

Apresento também o resultado esperado do *output* do programa:

```
    Result of '16
    ' is 16
    Result of '(1)
    ' is 1
    Result of '2+ 3
    ' is 5
    Result of '67 - (2 +3*4)
    ' is 53
    Result of '(9   -2)* (13 - 4 )
    ' is 63
```

## Autoria
![image](../images/a104541.png)

- Nome: José António Fernandes Alves Lopes
- Número Mecanográfico: a104541
- Data: 2025/03/22
