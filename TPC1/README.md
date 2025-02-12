# PL2025 - TPC1
## Descrição do problema
Este documento apresenta a documentação relativa ao primeiro trabalho de casa
proposto pela cadeira de processamento de linguagens. Foi pedido um programa,
escrito em Python, que cumprisse os seguintes requisitos:

- Pretende-se um programa que some todas as sequências de dígitos que encontre
num texto;
- Sempre que encontrar a *string* "Off" em qualquer combinação de maiúsculas e
minúsculas, esse comportamento é desligado;
 - Sempre que encontrar a *string* "On" em qualquer combinação de maiúsculas e
 minúsculas, esse comportamento é novamente ligado;
 - Sempre que encontrar o caráter "=", o resultado da soma é colocado na saída.

 Sequências de dígitos separadas por um delimitador (vírgula ou ponto) não são
 interpretadas pelo programa como um número com casas decimais; todas as
 operações no programa são realizadas sobre inteiros. O programa pode ser
 consultado no ficheiro ```summation_on_off.py```.

## Metodologia

Apenas como modo de consolidar a metodologia apresentada em aula, procurei
utilizar um processo iterativo caracterizado por 3 fases: análise léxica,
análise sintática e análise semântica. Reparo desde já que, apesar de ser esta
a intenção inicial, acabei por não realizar análise sintática, visto que não
existem regras que restrinjam a forma como os diferentes *tokens* são
combinados.

## Análise léxica

A análise léxica é concretizada na função ```lexical_analysis```, que tem como
objetivo pesquisar o texto introduzido no programa, carater a carater, e extrair
todas as palavras relevantes. Existem quatro destas, os símbolos ```Off``` e
```On```, em qualquer combinação de maiúsculas e minúsculas, o símbolo ```=``` e
sequências de dígitos. Foi construído um tipo ```Enum``` para identificar cada
símbolo:

```py
    class TokenType(Enum):
        ON     = auto()
        OFF    = auto()
        EQUALS = auto()
        NUMBER = auto() # Sequência de dígitos
```

As palavras são descritas em código como *tokens*, sendo ```Token``` um tipo de
dados que permite identificar qualquer um dos quatro símbolos já descritos. Para
o caso de uma sequência de dígitos, à qual é atribuída o ```TokenType```
```NUMBER```, o campo ```value``` é preenchido com o inteiro que esta
representa.

```py
    class Token:
        type: TokenType
        value: int | None = None
```

A sequência de palavras, ou *tokens*, resultantes do tratamento de texto
é devolvida à função que chamou o analisador léxico, e utilizada como *input*
para o analisador semântico.

## Análise semântica

A análise semântica é realizada na função ```semantic_analysis```, esta itera
pelos *tokens* obtidos na fase anterior, e aplica o comportamento desejado da
aplicação, como caracterizado na descrição do problema.

## Resultados e Conclusão

O programa pode ser executado da seguinte forma:

```
$ python3 summation_on_off.py
```

Já com o programa em execução, o utilizador pode introduzir qualquer texto que
deseje analisar, sendo que este deve ser terminado pelo carater *newline*. Para
que o programa proceda com a análise, deve ainda ser-lhe enviado um
sinal ```EOF```, de modo a indicar o fim da *stream* de comunicação pelo
*stdin*. Tal pode ser feito ao pressionar ```ctrl+d```.

A correção do programa foi verificada para o texto de exemplo descrito de
seguida:

```
OfF Dr1f71ng on a s7r24am = a 5tream
603sc1ously = it oFf s88ms =
A11 ON wha7 = remains = On
Eg0 bra1n =, man-mad2 3hame =

```

O resultado esperado da análise deste excerto, apresentado abaixo, é
coincidente com o *output* do programa. Este foi, por isso, dado como correto
para o *input* dado.

```
31
640
640
647
647
648
653
```

## Autoria
![image](../images/a104541.png)

- Nome: José António Fernandes Alves Lopes
- Número Mecanográfico: a104541
- Data: 2025/02/12
