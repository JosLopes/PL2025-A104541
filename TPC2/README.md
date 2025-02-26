# PL2025 - TPC2
## Descrição do problema

Este documento apresenta a documentação relativa ao segundo trabalho de casa
proposto pela cadeira de processamento de linguagens. Foi pedido um programa,
escrito em Python, que cumprisse os requisitos presentes neste
[enunciado](tpc2.pdf).

## Metodologia

Para obter os resultados pretendidos foi, primeiramente, criado um *dataset* em
memória, a partir da leitura e interpretação do ficheiro *csv* [obras](obras.csv).
Para tal recorri a expressões regulares, estas aplicadas a funções da biblioteca
```re```.

## Análise e Interpretação do Ficheiro CSV

Primeiramente, é relevante estabelecer a estrutura de dados utilizada para
guardar a informação em memória. Optei por uma abordagem simples, pelo que o
*dataset* completo nada mais é do que um *set* de elementos da classe
```MusicRecord```, cuja definição é apresentada abaixo:

```py
@dataclass
    class MusicRecord:
        nome: str
        desc: str
        anoCriacao: int
        periodo: str
        compositor: str
        duracao: str
        _id: str
```

Estamos agora em condições de preencher a estrutura de dados. Para tal, foi
estabelecida uma leitura do ficheiro em duas partes. A primeira procura
*match* com uma linha *csv* completa, isto é, uma sequência de 7 elementos
separados pelo delimitador ';', que compõem um objeto da classe
```MusicRecord```. A segunda procura extrair cada elemento individual das
linhas *csv* já capturadas, de modo a ser realmente possível construir estes
objetos.

Foram então usadas duas expressões regulares como forma de abordar os dois
problemas, ```[^ \n]+?(?:[^;]+;){6}[^\n]+``` e ```\"(?:[^\"]|\"\")*\"|[^;]+```.
A primeira diz respeito à procura de linhas *csv* completas, que podem ser
identificadas da seguinte forma: começam por zero ou mais carateres que não
*whitespace* ou *newline* (```[^ \n]+?```), seguidos por uma sequência de
um ou mais carateres que terminam no delimitador ';', sendo que esta sequência
se deve repetir por seis vezes, o que corresponde aos seis primeiros elementos
de uma linha *csv* completa (```(?:[^;]+;){6}```); por fim, basta identificar
o sétimo elemento, que terá um ou mais carateres que não o *newline*, que indica
o término da linha (```[^\n]+```).

A segunda expressão procura capturar os elementos que compõem um objeto da
classe ```MusicRecord``` numa linha *csv*, estes podem ser facilmente
identificáveis pela expressão regular ```[^\n]+```, já apresentada antes. No
entanto, é também necessário tratar os casos em que o delimitador ';' aparece
entre aspas, pelo que nestes contextos o seu comportamento normal deve ser
ignorado, isto é, deve ser tratado como qualquer outro carater. É então
acrescentada a expressão ```(\"(?:[^\"]|\"\")*\")``` como alternativa,
originando na expressão final ```\"(?:[^\"]|\"\")*\"|[^;]+```. A utilização
destas expressões, assim como o resto do processo da construção do *dataset*,
pode ser consultado de seguida:

```py
    res = list()

    matches = re.findall(r"[^ \n]+?(?:[^;]+;){6}[^\n]+", plaincsv)

    for i in range(1, len(matches)):
        elems = re.findall(r"\"(?:[^\"]|\"\")*\"|[^;]+", matches[i])

        if len(elems) == 7:
            res.append(MusicRecord(elems[0],
                                   elems[1],
                                   elems[2],
                                   elems[3],
                                   elems[4],
                                   elems[5],
                                   elems[6]))
```

As interrogações propostas também foram implementadas, mas não existe qualquer
interesse, do ponto de vista da cadeira, em analisar a sua implementação.

## Resultados e Conclusão

O programa pode ser executado da seguinte forma:

```
$ python3 csv_dataset_interpreter.py
```

As interrogações propostas são apresentadas na tela e não apresentam
incongruências notórias com o que seria esperado, pelo que dei o programa como
correto, apesar de não estar devidamente testado.

## Autoria
![image](../images/a104541.png)

- Nome: José António Fernandes Alves Lopes
- Número Mecanográfico: a104541
- Data: 2025/02/26
