import numpy as np

#min max sort mean num dot
precos = np.array([25, 20, 35, 30, 40])
quantidades = np.array([5, 10, 25, 30, 40])

produto_mais_caro = np.max(precos)
produto_mais_barato = np.min(precos)
print('produto mais caro = {} e mais barato = {}'.format(produto_mais_caro, produto_mais_barato))

precos_ordenadas = np.sort(precos)
print(precos_ordenadas)

precos_media = np.mean(precos)
print(precos_media)

print(quantidades * precos)

print(np.sum(quantidades * precos))

#dot = a soma da quantidades * preços = sum(qtde * precos) == np.dot
print(np.dot(quantidades, precos))

