# Exercício 01 - Entendendo operações básicas
## O que são operações?
Operações são tudo que envolve uma variável, existem diferentes tipos, como por exemplo: operações matemáticas, operações com strings, operações de comparação, operações lógicas...

## Operações matemáticas
Operações matemáticas são as operações que envolvem números, como por exemplo: soma, subtração, multiplicação, divisão, potenciação, porém, ainda existem algumas operações não tanto comuns, como por exemplo: resto da divisão, divisão inteira e raiz quadrada. Abaixo temos alguns exemplos:

    # Soma
    1 + 1 # 2
    # Subtração
    1 - 1 # 0
    # Multiplicação
    1 * 1 # 1
    # Divisão
    1 / 1 # 1
    # Potenciação
    1 ** 1 # 1
    # Resto da divisão
    1 % 1 # 0
    # Divisão inteira
    7 // 2 # 1
    # Raiz quadrada
    9 ** 0.5 # 3

## Operações com strings
Operações com strings são as operações que envolvem strings, como por exemplo: concatenação, repetição, porém, ainda existem algumas operações não tanto comuns, como por exemplo: divisão de strings. Abaixo temos alguns exemplos:

    # Concatenação
    'a' + 'b' # 'ab'
    # Repetição
    'a' * 3 # 'aaa'
    # Divisão de strings
    'abc' / 'a' # ['b', 'c']

## Operações de comparação
Operações de comparação normalmente serão responsáveis pela criação de um valor Bollean, isso é, caso vc utilize print(2>1) terá a resposta True. Estas operações dentro de IF's são responsáveis tomar decisões dentro do código. Abaixo temos alguns exemplos:

    # Maior que
    2 > 1 # True
    # Menor que
    1 < 2 # True
    # Igual a
    1 == 1 # True
    # Diferente de
    1 != 1 # False
    # Maior ou igual a
    1 >= 1 # True
    # Menor ou igual a
    1 <= 1 # True

## Operações de atribuição
Operações de atribuição envolvem calcular um valor e depois atribuir para uma variável, na mesma linha, alguns exemplos são:

    # Soma
    a = 1
    a += 1 # a = 2
    # Subtração
    a = 1
    a -= 1 # a = 0
    # Multiplicação
    a = 1
    a *= 1 # a = 1
    # Divisão
    a = 1
    a /= 1 # a = 1
    # Potenciação
    a = 1
    a **= 1 # a = 1
    # Resto da divisão
    a = 1
    a %= 1 # a = 0
    # Divisão inteira
    a = 7
    a //= 2 # a = 1
    # Raiz quadrada
    a = 9
    a **= 0.5 # a = 3

## Operações lógicas
Operações lógicas são utilizadas para acrescimento de complexidade das operações de comparação. Normalmente usamos os três principais: and, or e not. And é utilizado quando queremos que, para aparecer True, duas comparações precisam ser True, isso é, True and True, True e true, traduzindo. Or é traduzido do inglês para 'ou', tem a função oposta do 'and', com o 'or' mesmo que uma das avalições seja False, o resultado ainda é True. Por fim, 'not' é a negação do que está lá, se 1==1 daria True, not 1==1 vai dar False; se usar dois not, como not not 1==1, um nega o outro. Quando formos falar de IF's vamos usar bastante isso. Abaixo temos alguns exemplos:

    # and
    True and True # True
    # or
    True or False # True
    # not
    not True # False


## Exemplo
No arquivo exemplo.py tu vais encontrar exemplos de tudo que foi falado aqui, além de alguns exemplos de IF's, que serão explicados no próximo exercício.