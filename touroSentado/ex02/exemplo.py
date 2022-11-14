# Usando a função de pois de definí-la
def usoDeFuncao():
    print("\nusoDeFuncao")
    def minha_funcao(parametro1, parametro2):
        print(parametro1)
        print(parametro2)
    minha_funcao(1, 2)

# Tentar usar a função antes de definí-la
def erroDeOrdem():
    print("\nerroDeOrdem")
    minha_funcao(1, 2)
    def minha_funcao(parametro1, parametro2):
        print(parametro1)
        print(parametro2)

# Só printa qualquer coisa colocada como parametro
def printarAlgo(lista):
    print("\nPrintar Algo")
    print(lista)

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