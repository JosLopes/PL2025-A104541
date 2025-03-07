# PL2025 - TPC4
## Descrição do problema

Este documento apresenta a documentação relativa ao quarto trabalho de casa
proposto pela cadeira de processamento de linguagens. Foi pedido um analisador
léxico, escrito em python, que cumprisse os requisitos do [enunciado](tpc4.pdf).

## Metodologia

Optei por utilizar a biblioteca ```ply``` para realizar este trabalho, pelo que
apenas necessitei de identificar os símbolos da linguagem e construir expressões
regulares que capturassem cada um deles. Foi estabelecida a seguinte sequência
de símbolos, ou *tokens*:

```py
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
```

De modo a garantir a correta ordem de captura dos *tokens*, especifiquei cada
um deles através de uma função. As funções, relativas a cada *token*, seguem a
mesma ordem que a lista apresentada acima. Foram também especificados
comportamentos para carateres a ignorar, ```t_ignore```, para carateres
*newline*, ```t_newline```, e para carateres ilegais, ```t_error```. De seguida
apresento umas das funções definidas, como exemplo:

```py
    def t_STR(t):
        r'\"(?P<CONTENT>.*?)\"(?:@(?P<LAN>\w+))?'
        t.value = re.match(t_STR.__doc__, t.value).groupdict()
        return t
```

Esta função apresenta uma expressão regular em *docstring*, que será utilizada
pelo ```ply``` para encontrar uma correspondência no texto de origem. Se for
encontrado algum *match*, prosseguimos para a identificação dos dois campos
presentes na *string*, o seu conteúdo e a sua linguagem, seguido pela
respetiva atribuição à variável ```t.value```. O *token* está, por fim, bem
construído, pelo que é devolvido.

## Resultados e Conclusão

O programa pode ser executado da seguinte forma:

```
$ python3 lexical_analyzer.py <query_file_path>
```

Este programa foi verificado para a frase de exemplo descrita no
[enunciado](tpc4.pdf), pelo que o considerei correto. O resultado da execução do
programa pode ser consultado abaixo, e corresponde ao que seria esperado.

```
    LexToken(COMMENT,'# DBPedia: obras de Chuck Berry',1,0)
    LexToken(SELECT,'select',3,33)
    LexToken(VARIABLE,'?nome',3,40)
    LexToken(VARIABLE,'?desc',3,46)
    LexToken(WHERE,'where',3,52)
    LexToken(LBRACE,'{',3,58)
    LexToken(VARIABLE,'?s',4,64)
    LexToken(PROPERTY,'a',4,67)
    LexToken(PROPERTY,'dbo:MusicalArtist',4,69)
    LexToken(POINT,'.',4,86)
    LexToken(VARIABLE,'?s',5,92)
    LexToken(PROPERTY,'foaf:name',5,95)
    LexToken(STR,{'CONTENT': 'Chuck Berry', 'LAN': 'en'},5,105)
    LexToken(POINT,'.',5,122)
    LexToken(VARIABLE,'?w',6,128)
    LexToken(PROPERTY,'dbo:artist',6,131)
    LexToken(VARIABLE,'?s',6,142)
    LexToken(POINT,'.',6,144)
    LexToken(VARIABLE,'?w',7,150)
    LexToken(PROPERTY,'foaf:name',7,153)
    LexToken(VARIABLE,'?nome',7,163)
    LexToken(POINT,'.',7,168)
    LexToken(VARIABLE,'?w',8,174)
    LexToken(PROPERTY,'dbo:abstract',8,177)
    LexToken(VARIABLE,'?desc',8,190)
    LexToken(RBRACE,'}',9,196)
    LexToken(LIMIT,'LIMIT',9,198)
    LexToken(NUM,1000,9,204)
```

## Autoria
![image](../images/a104541.png)

- Nome: José António Fernandes Alves Lopes
- Número Mecanográfico: a104541
- Data: 2025/03/07
