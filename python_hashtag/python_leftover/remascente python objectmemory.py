# is = pergunta se ambas estão apontando ao mesmo objeto

# a = "banana"

# b = "banana"

# c = "maça"
# ab = a is b
# print(ab)

# = true


# minha_lista = [
#     1, 2, 3,
#     4, 5, 6,
#     ]


# Para operações matemáticas, divida as linhas antes dos operadores matemáticos, não depois (em algumas linguagens, 
# a convenção é invertida, mas há boas razões para o estilo pythônico):
# lucro = (vendas
#          + dividendos
#          - juros_divida
#          - salarios)


# lista1 = ["carro", "ônibus", "barco", "bicicleta"]
# lista2 = ["carro", "ônibus", "barco", "bicicleta"]
# lista3 = ["carro", "barco"]

# lista4 = lista3 is lista2

# print(lista4)

# = false



# lista1 = ["carro", "ônibus", "barco", "bicicleta"]
# lista2 = ["carro", "ônibus", "barco", "bicicleta"]
# lista3 = ["carro", "barco"]

# lista4 = lista1 is lista3

# print(lista4)

# False

lista1 = ["carro", "ônibus", "barco", "bicicleta"]
lista2 = ["carro", "ônibus", "barco", "bicicleta"]
lista3 = ["carro", "barco"]

lista4 = lista2 is lista3

print(lista4)


# No exemplo apresentado, a comparação lista1 is lista2 retorna False porque as variáveis lista1 e lista2 apontam para objetos diferentes na memória, 
# apesar de terem o mesmo conteúdo. Ao usar o operador is, estamos comparando se as duas variáveis se referem ao mesmo objeto na memória. Para
# comparar se duas listas possuem o mesmo conteúdo, devemos utilizar o operador de igualdade (==), como por exemplo




# Memória do computador é uma
# sequência muito longa de bytes.


# O objeto é guardado dentro
# da memória e uma variável guarda o endereço de memória onde o ele está
# armazenado, ou seja, a variável aponta para a posição de memória onde o objeto
# está armazenado.


lista1 = ["carro", "barco"]
lista2 = [lista1] * 3
lista3 = lista1 * 3
lista1[1] = "metrô"

print(lista3)

# r: ['carro', 'barco', 'carro', 'barco', 'carro', 'barco']

# Quando você cria uma lista, como lista1 = ["carro", "barco"], e então cria uma nova lista lista2 = [lista1] * 3, você está criando uma nova lista que 
# contém três referências para a lista original lista1. Ou seja, lista2 é uma lista que contém três vezes a mesma referência para a lista lista1.

# Por outro lado, quando você multiplica uma lista por um número inteiro, como em lista3 = lista1 * 3, você está criando uma nova lista que contém três 
# cópias dos elementos da lista original lista1. Nesse caso, as cópias dos elementos da lista lista1 são adicionadas à nova lista lista3, e não há referências
# à lista lista1 dentro dela.
# Então, quando você altera o elemento lista1[1], isso não afeta a lista lista2, pois lista2 contém apenas referências à lista1. No entanto, como a lista 
# lista3 contém cópias dos elementos da lista original lista1, ela é afetada pela alteração em lista1[1].