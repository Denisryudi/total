lista = ['ipad', 'iphone x', 'apple tv']
lista2 = lista

lista[1] = 'iphone 11'

print(lista2)

"""### Agora copiando:"""

lista = ['ipad', 'iphone x', 'apple tv']
lista2 = lista.copy()

lista[1] = 'iphone 11'

print(lista2)