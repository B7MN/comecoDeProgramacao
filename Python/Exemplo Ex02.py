# Usando a função de pois de definí-la
def usoDeFuncao():
    print("\nusoDeFuncao")
    def minha_funcao(parametro1, parametro2):
        print(parametro1)
        print(parametro2)
    minha_funcao(1, 2)
# Exemplo de if/else
print("\nExemplo de if/else")
a = 3
b = 2
if a > b:
    print("a é maior que b")
else:
    print("a é menor que b")

# Tentar usar a função antes de definí-la
def erroDeOrdem():
    print("\nerroDeOrdem")
    minha_funcao(1, 2)
    def minha_funcao(parametro1, parametro2):
        print(parametro1)
        print(parametro2)
# Exemplo de if/elif/else
# Elif é um Else e um If juntos, ele só é executado se o if anterior for falso
# mas verifica se a sua condiação é verdadeira, neste caso, temos 2 condições
# a primeira é se A é maior que B, se for, ele printa "a é maior que b"
# se não for, ele verifica se A é igual a B, se for, ele printa "a é igual a b"
# caso nenhuma das coisas anteriores funcione, ele printa "a é menor que b"
# pois se um número não é maior nem igual a outro, ele é menor
print("\nExemplo de if/elif/else")
a = 3
b = 2
if a > b:
    print("a é maior que b")
elif a == b:
    print("a é igual a b")
else:
    print("a é menor que b")

# Só printa qualquer coisa colocada como parametro
def printarAlgo(lista):
    print("\nPrintar Algo")
    print(lista)
# Exemplo de while
# O while é um loop, ele executa um bloco de código enquanto uma condição for verdadeira
# neste caso, enquanto a for menor que 10, ele printa o valor de a e soma 1 a ele
print("\nExemplo de while")
a = 0
while a < 10:
    print(a)
    a += 1

# Função que soma dois números
def somaDoisValores(a, b):
    print("\nsomaDoisValores")
    # Se não tiver nenhum print dentro da função, não aparece nada, mas ela retorna o valor
    return a + b

# Para todas as funções rodarem é necessário comentar a segunda função com erro
def main():
    usoDeFuncao()
    erroDeOrdem()
    lista = [1, 2, 3, 4, 5]
    printarAlgo(lista)
    soma = somaDoisValores(1, 2)

    # Printar soma dentro da função ou usando somente print() não tem diferença
    printarAlgo(soma)
    print(soma)

print("\nInício do programa")
main()
print("\nFim do programa")
# Exemplo de for
print("\nExemplo de for")
# O for é um loop, ele executa um bloco de código para cada elemento de uma lista
# neste caso, para cada elemento da lista, ele printa o elemento
lista = [1, 2, 3, 4, 5]
# podemos traduzir a linha de baixo para
# PARA elemento NA lista, os elementos são os valores da lista
for elemento in lista:
    print(elemento)