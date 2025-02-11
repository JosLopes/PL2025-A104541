# Manifesto TPC1
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
 operações no programa são realizadas sobre inteiros.

## Metodologia

Apenas como modo de consolidar a metodologia apresentada em aula, procurei
utilizar um processo iterativo caracterizado por 3 fases: a análise léxica, que
examina a sequência de carateres original e procura encontrar as palavras, ou
*tokens*, que a compõem; a análise sintática, que constrói a estrutura
gramatical a partir da sequência de palavras (árvore sintática); e, por fim, o
analisador semântico, que atribuí significado aos elementos da árvore sintática.
Acabei, no entanto, por não realizar a análise sintática, visto que não existem
regras que restrinjam a forma como as diferentes palavras são combinadas.

## Análise léxica

## Análise semântica

## Resultados e Conclusão

```
hello
```