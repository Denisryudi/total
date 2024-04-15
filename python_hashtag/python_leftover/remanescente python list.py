
# frutas_exoticas = ["jaboticaba", "cupuaçu", "graviola"]

# for fruta in frutas_exoticas:
#     print ("eu adoro", fruta)

# r:eu adoro jaboticaba
# eu adoro cupuaçu     
# eu adoro graviola


# for i in range(0, 20, 3):
#     print(i)

# r: 0
# 3
# 6
# 9
# 12
# 15
# 18

# numeros = range(100, 0, -5)

# for x in numeros:
#     print(x)

# r: 100
# 95
# 90
# 85
# 80
# 75
# 70
# 65
# 60
# 55
# 50
# 45
# 40
# 35
# 30
# 25
# 20
# 15
# 10
# 5
# animais = ["gato", "cachorro", "papagaio", "arara", "jacaré"]
# for x in animais:
#     print("--> ", x)

# -->  gato
# -->  cachorro
# -->  papagaio
# -->  arara
# -->  jacaré

# animais = ["gato", "cachorro", "papagaio", "arara", "jacaré"]
# for x in range(len(animais)):
#     print("--> ", x)

# r: -->  0
# -->  1
# -->  2
# -->  3
# -->  4


# animais = ["gato", "cachorro", "papagaio", "arara", "jacaré"]

# for x in range(len(animais)):
#     print("--> ", animais[x])

# -->  gato
# -->  cachorro
# -->  papagaio
# -->  arara
# -->  jacaré  



# for i in range(16,4,-3):
# 	print(i)
        
# r:16
# 13
# 10
# 7
# valores = []
# for i in range(1, 10):
#     if i % 2 == 0:
#         valores.append(i)

# print(valores)

# r:[2, 4, 6, 8]
# valores = []
# for i in range(0, 10, 2):
#     valores.append(i)
# print(valores)




# animais = ["gato", "cachorro", "papagaio",
# "arara", "jacaré"]
# animais[2] = animais.append("piriquito")

# print(animais)

# r = ['gato', 'cachorro', None, 'arara', 'jacaré', 'piriquito']


# animais = ["gato", "cachorro", "papagaio",
# "arara", "jacaré"]
# animais[-3] = "piriquito"

# print(animais)
# r = ['gato', 'cachorro', 'piriquito', 'arara', 'jacaré']



# animais = ["gato", "cachorro", "papagaio",
# "arara", "jacaré"]

# animais[2] = "piriquito"

# print(animais)

# lista1 = ["vermelho" ,"verde", "azul"]


# lista2 = lista1

# lista2[0] = "rosa"

# print(lista2)

# r= ['rosa', 'verde', 'azul']

# def clone (lista):
#     clone=[]
#     for objeto in lista:
#         clone.append(objeto)
#     return clone

# lista2[0] = "branca"

# print(lista2)

# modo mais facil \/

# Fatiamento cria uma nova lista

# lista1[ini:fim]
# lista1[ini:]
# lista1[:fim]
#          lista1[:] = clone da lista 


# lista1 = ["vermelho" ,"verde", "azul"]

# lista2 = lista1[:] #


# lista2[0] = "rosa"

# print(lista2)
# print(lista1)



# lista2[0] = "rosa"

# r=['rosa', 'verde', 'azul']
# ['vermelho', 'verde', 'azul']

# pertinência


# lista1 = ["vermelho" ,"verde", "azul"]

# lista2 = lista1[:] #


# lista2[0] = "rosa"

# print(lista2)
# print(lista1)


# if "cinza" in lista1:
#     print("esta")
# else:
#     print("não esta")

    # append = acrescenta ao final de uma lista existente um novo elemento

# lista1.append("silver")

# print(lista1)

# del lista1[0:4]

# print(lista1)

# r= ['vermelho', 'verde', 'azul', 'silver']
# ['silver']

# lista1.append("silver")

# print(lista1)

# del lista1[1:4]

# print(lista1)

# r= ['vermelho', 'verde', 'azul', 'silver']
# ['vermelho']

# :12 =0 a 11
# 12: = 11 a 0


# carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
# carnes2 = []
# for cns in carnes:
#     carnes2.append(cns) #cns age como a essência de "carnes" 
# carnes2.append("ponta de alcatra")


# print(carnes)

# print(carnes2)

# = ['picanha', 'alcatra', 'filé mignon', 'cupim']
# ['picanha', 'alcatra', 'filé mignon', 'cupim', 'ponta de alcatra']


carnes1 = ["picanha", "alcatra"]
carnes2 = ["filé mignon", "cupim", "ponta de alcatra"]
carnes3 = carnes2 + carnes1

print(carnes1)
print(carnes2)
print(carnes3)