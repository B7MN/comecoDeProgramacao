# Exercício 02 - Entendendo If's, while e ForLoop
Existem algumas vezes que queremos percorrer toda um conjunto de dados e verificar se algum deles bate com alguma informação que temos, por exemplo, se um número é par ou ímpar, se um número é maior que outro, se uma string é igual a outra, etc. Para isso, utilizamos If's, While e ForLoop.

## If's
If's são responsáveis por verificar se uma condição é verdadeira ou falsa, caso seja verdadeira, ele executa o código que está dentro do If, caso seja falsa, ele executa o código que está dentro do Else. Abaixo temos alguns exemplos:

    # Verificando se um número é par
    numero = 2
    if numero % 2 == 0:
        print('O número é par')
    else:
        print('O número é ímpar')
    # O número é par

    # Verificando se um número é maior que outro
    numero1 = 2
    numero2 = 1
    if numero1 > numero2:
        print('O número 1 é maior que o número 2')
    else:
        print('O número 2 é maior que o número 1')
    # O número 1 é maior que o número 2

    # Verificando se uma string é igual a outra
    string1 = 'a'
    string2 = 'a'
    if string1 == string2:
        print('As strings são iguais')
    else:
        print('As strings são diferentes')
    # As strings são iguais

## While
While é responsável por verificar se uma condição é verdadeira ou falsa, caso seja verdadeira, ele executa o código que está dentro do While, caso seja falsa, ele não executa o código que está dentro do While. Abaixo temos alguns exemplos:

    # Verificando se um número é par, enquanto ele for par, ele continua verificando, como ele acrescenta o valor, ele vai rodar somente uma vez.
    numero = 2
    while numero % 2 == 0:
        print('O número é par')
        numero += 1
    # O número é par

    # Verificando se um número é maior que outro, neste caso ele também vai rodar somente uma vez, pois o número 2 é maior até que seja reduzido em 1.
    numero1 = 2
    numero2 = 1
    while numero1 > numero2:
        print('O número 1 é maior que o número 2')
        numero1 -= 1
    # O número 1 é maior que o número 2

    # Verificando se uma string é igual a outra, neste caso, o while vai permanecer rodando indefinidamente, pois não existe nenhuma alteração dentro dele para que ele pare de rodar.
    string1 = 'a'
    string2 = 'a'
    while string1 == string2:
        print('As strings são iguais')
    # As strings são iguais

## ForLoop
ForLoop é responsável por percorrer um conjunto de dados, como uma lista, um dicionário, uma tupla, etc. Abaixo temos alguns exemplos:

    # Percorrendo uma lista
    lista = [1, 2, 3, 4, 5]
    for item in lista:
        print(item)
    # 1
    # 2
    # 3
    # 4
    # 5

    # Percorrendo um dicionário
    dicionario = {'a': 1, 'b': 2, 'c': 3}
    for item in dicionario:
        print(item)
    # a
    # b
    # c

    # Percorrendo uma tupla
    tupla = (1, 2, 3, 4, 5)
    for item in tupla:
        print(item)
    # 1
    # 2
    # 3
    # 4
    # 5

    # Percorrendo uma string, as string são um conjunto de caracteres, então, ele vai percorrer cada caractere da string, como uma lista.
    string = 'abcde'
    for item in string:
        print(item)
    # a
    # b
    # c
    # d
    # e

    # Percorrendo um range, aqui ele cria uma lista com os números que começam no primeiro valor e terminam antes do segundo, isso é, de 1 a 5.
    for item in range(1, 6):
        print(item)
    # 1
    # 2
    # 3
    # 4
    # 5

    # Percorrendo um range com passo, de 2 em 2, a lista ficou [1, 3, 5]
    for item in range(1, 6, 2):
        print(item)
    # 1
    # 3
    # 5

    # Percorrendo um range com passo negativo
    for item in range(5, 0, -1):
        print(item)
    # 5
    # 4
    # 3
    # 2
    # 1

## Exemplo
No arquivo exemplo.py temos uma série de exemplos do que foi falado acima, interessante ver como poucas linhas podem fazer muita coisa.

## Exercício
