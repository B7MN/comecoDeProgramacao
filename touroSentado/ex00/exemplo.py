# função type(AlgoAquiDentro) vai retornar o tipo de dado que está dentro dos parênteses
# Exemplo:
print(type(1)) # Vai retornar <class 'int'>, porque o número 1 é um inteiro
print(type(1.0)) # Vai retornar <class 'float'>, porque o número 1.0 é um float
print(type("1")) # Vai retornar <class 'str'>, porque o número "1" é uma string

# A diferença entre lista "[]", tuplos "()" e sets "{}"

# Listas são ordenados mutáveis, isso é, eles funcionam por index e você pode alterar, exlui ou adicionar elementos.
# Normalmente também usamos listas para armazenar dados de um mesmo tipo, como por exemplo, uma lista de números inteiros.
print(type( [1, 2, 3] )) # Vai retornar <class 'list'>, porque a lista [1, 2, 3] é uma lista

# Tuplos são ordenados imutáveis, isso é, eles funcionam por index e você não pode alterar, exlui ou adicionar elementos.
# Normalmente também usamos tuplos para armazenar dados de um mesmo tipos diferentes, como por exemplo, uma lista de números inteiros e strings.
print(type( (1, 2, 3) )) # Vai retornar <class 'tuple'>, porque a tupla (1, 2, 3) é uma tupla

# Sets são desordenados e não indexados, isso é, eles não funcionam por index e você não pode alterar, exlui ou adicionar elementos.
# Normalmente também usamos sets para armazenar dados de um mesmo tipo, como por exemplo, uma lista de números inteiros.
print(type( {1, 2, 3} )) # Vai retornar <class 'set'>, porque o conjunto {1, 2, 3} é um conjunto

print(type({1: "a", 2: "b", 3: "c"})) # Vai retornar <class 'dict'>, porque o dicionário {1: "a", 2: "b", 3: "c"} é um dicionário

