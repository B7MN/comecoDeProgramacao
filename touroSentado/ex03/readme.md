# Exercício 03 - Entendendo funções
## O que são funções?
Funções são a base de qualquer linguagem de programação, elas são a únicas coisas que existem além de variáveis, alguns exemplos de funções são:
- print() - Imprime algo na tela;
- input() - Solicita ao usuário algum valor de entrada, usamos ela para pegar o número naquele jogo de adivinhar número aleatório;
- type() - Retorna o tipo de dado de uma variável, se é int, float, string, etc;

Apesar do Python ter quase infinitas funções de milhões de pessoas das comunidades de programadores na internet, as vezes precisamos fazer algo em específico, para resolver um problema específico, e para isso precisamos criar nossas próprias funções, vamos fazer isso agora.

## Criando/definindo uma função
Para criar uma função, usamos a palavra reservada `def`, seguida do nome da função, e, se for necessário, entre parênteses os parâmetros que a função vai receber. Por fim dois pontos `:`. Veja o exemplo abaixo:

    def minha_funcao(parametro1, parametro2):
        # Código da função

Parametros são variáveis que a função vai receber, e que podem ser usadas dentro da função, como se fossem variáveis normais. Veja o exemplo abaixo:

    def minha_funcao(parametro1, parametro2):
        print(parametro1)
        print(parametro2)

Também não podemos usar uma funções antes de defini-la, por exemplo, se eu tentar usar a função `minha_funcao` antes de defini-la, o Python vai dar um erro, veja o exemplo abaixo:

    minha_funcao(1, 2)
    def minha_funcao(parametro1, parametro2):
        print(parametro1)
        print(parametro2)

Outra informação importante é a identação, ela é muito importante em Python, e é usada para definir o que está dentro da função, e o que está fora. Veja o exemplo abaixo:

    def minha_funcao(parametro1, parametro2):
        print(parametro1)
        print(parametro2)

    print("Estou fora da função")
    minha_funcao("Estou dentro da função", "E também estou dentro da função")

Por fim, o retorno de uma função é o que ela vai te dar depois dos procedimentos que ela faz, por exemplo, se eu tenho uma função que soma dois números, o retorno dela é a soma dos dois números, veja o exemplo abaixo:

    a = 1
    b = 2
    def somaDoisValores(a, b):
        return a + b

    c = somaDoisValores(a, b)
    print(c) # Vai imprimir 3


## Exemplo
No arquivo 'exemplo.py' temos um conjunto de funções estão sendo definidas em cima e utilizadas dentro da função main, que, por acaso, também está definida acima e sendo utilizada no final do arquivo.


## Exercício
No arquivo 'main.py' temos duas funções para serem completadas, somaDoisValores e printarAlgo.

