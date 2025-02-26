# PL2025 - TPC3
## Descrição do problema
Este documento apresenta a documentação relativa ao terceiro trabalho de casa
proposto pela cadeira de processamento de linguagens. Foi pedido um conversor de
MarkDown para HTML, escrito em python, que tivesse em conta os argumentos
descritos no [enunciado](tpc3-1.pdf):

## Metodologia

Para abordar esta proposta decidi partir o problema em quatro: um conversor de
cabeçalhos, um conversor de *bold* e itálico, um conversor de listas enumeradas e,
por fim, um conversor de links, tanto para imagens como para páginas *web*. Cada
um dá uso a expressões regulares e à operação de substituição da biblioteca
```re``` para resolver cada problema individualmente.

## Conversor de Cabeçalhos

O conversor de cabeçalhos é bastante simples, utiliza a expressão regular
```#{1,3}\s*(.+)``` para encontrar qualquer padrão que comece com pelo menos
um e até três símbolos '#' (```#{1,3}```), seguido/s por uma sequência de
espaços brancos de tamanho arbitrário (```\s*```). Qualquer carater que
proceda este padrão é capturado num grupo até ser encontrado um carater
*newline* (```(.+)```). Esta *string* capturada corresponde ao conteúdo que se
pretende preservar, pelo que é usada para completar a conversão, enquanto que
todos os outros carateres são substituídos/ removidos. O código do conversor
pode ser consultado abaixo:

```py
    re.sub(r'#{1,3}\s*(.+)', lambda match: f'<h1>{match.group(1)}<\\h1>', markdown)
```

## Conversor de *Bold* e Itálico

Já o conversor de *bold* e itálico, além de ser responsável por encontrar os
padrões que necessitam de substituição, tem também de distinguir entre os
dois delimitadores possíveis, ```*``` para itálico e ```**``` para *bold*.
Foi novamente utilizada uma expressão regular, desta vez a
```(\*\*|\*)(.+?)\```, de modo a identificar os padrões necessários. O primeiro
grupo de captura, ```(\*\*|\*)```, procura encontrar uma sequência de um ou dois
carateres '*'. Estes deverão ser seguidos por uma sequência de um, ou mais,
carateres que não o *newline*, ```(.+?)```, sequência esta que deve ser sucedida
pela mesma *string* que terá sido capturada no inicio, ```\1```. Foi utilizada
uma função secundária definida dentro da própria função de conversão, denominada
por ```replace_match```, de modo a ser possível aplicar o comportamento
desejado, que será diferente dependendo do delimitador encontrado:

```py
    def replace_match(match):
        delimiter = match.group(1)
        text = match.group(2)
        if delimiter == '**':
            return f'<b>{sub_bold_and_italic(text)}</b>'
        elif delimiter == '*':
            return f'<i>{sub_bold_and_italic(text)}</i>'
```

A expressão regular estudada no parágrafo anterior é aplicada da seguinte forma:

```py
    re.sub(r'(\*\*|\*)(.+?)\1', replace_match, markdown)
```

## Conversor de Listas Enumeradas

Devido à complexidade do problema que se procurava resolver com este conversor,
decidi o separar em dois sub-problemas. Primeiramente, procurei encontrar todas
as instâncias de listas enumeradas no conteúdo, de modo a conseguir adicionar
a tag ```<ol> ... </ol>```, antes de prosseguir com a conversão de cada elemento
na lista. Para tal, foi utilizada a expressão regular ```((\d+\.\s*.*\n)+)```,
que pode ser consultada no excerto de código apresentado abaixo. Esta captura
qualquer parte do conteúdo com pelo menos uma entrada de uma lista enumerada,
identificada por ```\d+\.\s*.*\n```. Pela expressão descrita, uma entrada pode
ser identificada por uma sequência de um ou mais digitos (```\d+```), seguida
por um ponto e uma sequência de zero ou mais espaços brancos (```\.\s*```). Por
sua vez, esta é seguida por uma sequência de zero ou mais carateres que não um
*newline* (```.*```). O *match* da entrada termina assim que for encontrado um
carater *newline*.

```py
    re.sub(r'((\d+\.\s*.*\n)+)', lambda match: f'<ol>\n{match.group(1)}</ol>\n', markdown)
```

Com cada lista identificada e corretamente convertida, podemos agora converter
cada entrada para o formato desejado. Para tal vamos reutilizar a expressão
regular que nos permitia identificar uma entrada de uma lista, com apenas duas
modificações. Queremos capturar o texto respetivo à descrição da entrada para o
poder aplicar na conversão, ou seja, precisamos de envolver a secção da
expressão que o captura da seguinte forma: ```\d+\.\s*(.*)\n```. Podemos
também remover o carater *newline* do final, uma vez que não o queremos
involver na operação de substituição. O código completo pode ser consultado de
seguida:

```py
    intermediate = re.sub(r'((\d+\.\s*.*\n)+)', lambda match: f'<ol>\n{match.group(1)}</ol>\n', markdown)
    re.sub(r'\d+\.\s*(.*)', lambda match: f'<li>{match.group(1)}</li>', intermediate)
```
## Conversor de *Links*

Semelhante ao conversor de *bold* e itálico, este também terá a responsabilidade
de distinguir diferentes *inputs* de modo a se comportar da forma desejada, uma
vez que este conversor irá aceitar dois tipos de *links*, para imagens e para
páginas *web*. A expressão regular utilizada é extremamente simples,
```(!?)\[(.*)\]\((.*)\)```, e procura encontrar os seguintes padrões de texto:
```[...](...)``` e ```?[...](...)```. Para providenciar os dois possíveis
comportamentos, foi feita uma função auxiliar dentro da própria função de
conversão, o código completo pode ser consultado de seguida:

```py
    def replace_match(match):
        start = match.group(1)
        text  = match.group(2)
        link  = match.group(3)

        if start == '!':
            return f'<img src="{link}" alt="{text}"/>'
        else: # start == nothing
            return f'<a href="{link}">{text}</a>'

    re.sub(r'(!?)\[(.*)\]\((.*)\)', replace_match, markdown)
```

## Resultados e Conclusão
O programa pode ser executado da seguinte forma:

```
$ python3 markdown-to-html.py <markdown-file>
```

Este programa foi verificado para um único *input*, pelo que se considera
correto para este exemplo particular, que pode ser consultado no ficheiro
[example.md](example.md). O resultado da execução do programa pode ser
consultado no ficheiro de *output*, [example.md.txt](example.md.txt), e está
de acordo com o output esperado, que foi realizado à mão e é descrito de
seguida:

```
<h1>Cabeçalho 1<\h1>
<h1>Cabeçalho 2<\h1>
<h1>Cabeçalho 3<\h1>

<ol>
<li>Mirror - Tarkovsky</li>
<li>12 Angry Men - Sidney Lumet</li>
<li>I Saw The TV Glow - Jane Schoenbrun</li>
</ol>

This is <b>bold text</b> and this is <i>italic text</i>.
This is <b>bold and <i>italic</i> text together</b>.

<ol>
<li>This is the start of another list</li>
<li>Another Item</li>
</ol>

This movie is <i>very</i> good and <b>free</b> to watch!!!: <a href="https://www.youtube.com/watch?v=NrMINC5xjMs">Tarkovsky's Mirror</a>
Imagem de um coelho: <img src="http://www.coellho.com" alt="imagem dum coelho"/>
```

## Autoria
![image](../images/a104541.png)

- Nome: José António Fernandes Alves Lopes
- Número Mecanográfico: a104541
- Data: 2025/02/26
