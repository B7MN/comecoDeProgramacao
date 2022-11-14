# Exercício 00 - Entendo variáveis
## O que são variáveis?
Variáveis são a base de qualquer linguagem de programação, elas são a únicas coisas que existem além de funções, alguns exemplos de implementação de variáveis são:
- a = 1 - A variável `a` recebe o valor inteiro 1;
- b = "Hello World" - A variável `b` recebe o valor string "Hello World";
- c = 1.5 - A variável `c` recebe o valor float 1.5;
- d = True - A variável `d` recebe o valor booleano True;

Mais pra frente vamos pegar tipos dados mais complexos, estes são os Objetos, eles funcionam parecido a um dicionário, mas vamos falar sobre eles mais pra frente.

## Classes/tipos de variáveis
Python é uma linguagem de tipagem dinâmica, isso significa que não precisamos declarar o tipo de dado que uma variável vai receber, o Python vai inferir o tipo de dado da variável automaticamente, veja o exemplo abaixo:

    a = 1
    print(type(a)) # Vai imprimir <class 'int'>
    a = "Hello World"
    print(type(a)) # Vai imprimir <class 'str'>
    a = 1.5
    print(type(a)) # Vai imprimir <class 'float'>
    a = True
    print(type(a)) # Vai imprimir <class 'bool'>


Variáveis em Python são case sensitive (sensíveis a caixa de letras), isso significa que `a` é diferente de `A`, veja o exemplo abaixo:

    a = 1
    A = 2
    print(a) # Vai imprimir 1
    print(A) # Vai imprimir 2

Por fim, existem variáveis globais e variáveis locais, variáveis globais são aquelas que estão fora de uma função, e variáveis locais são aquelas que estão dentro de uma função, veja o exemplo abaixo:

    a = 1 # Variável global
    def func():
        b = 2 # Variável local
        print(a) # Vai imprimir 1
        print(b) # Vai imprimir 2
    func()
    print(a) # Vai imprimir 1
    print(b) # Vai dar erro, pois a variável b não existe fora da função

A variável 'b' só existe dentro da função ''func''. Vamos tratar de funções no próximo exercício.

Obs: Python corre seus arquivos de cima pra baixo, então se você tentar usar uma variável antes de declarar ela, vai dar erro, veja o exemplo abaixo:

    print(a) # Vai dar erro
    a = 1

Isso é verdade para qualquer coisa, seja uma variável, função, classe, etc.

## Exemplo
Dentro do arquivo 'exemplo.py' tem um conjunsto de print(type()) que vão imprimir o tipo de dado de cada variável, além disso, tem uma descrição sobre listas, tuplos e dicionários.

## Exercício
Tu vais encontrar uma lista de variáveis no arquivo 'main.py', tu precisa completar o código para que ele imprima o tipo de cada variável, veja o exemplo abaixo:

    a = 1
    b = "Hello World"
    c = 1.5
    d = True
    print(type(a)) # Vai imprimir <class 'int'>
    print(type(b)) # Vai imprimir <class 'str'>
    print(type(c)) # Vai imprimir <class 'float'>
    print(type(d)) # Vai imprimir <class 'bool'>