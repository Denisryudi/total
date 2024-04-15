produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']

tamanho = len(produtos)
print(tamanho)

vendas = [100, 150, 100, 120, 70, 90, 80]




mais_vendido = max(vendas)
menos_vendido = min(vendas)

i = vendas.index(mais_vendido) #<---------------index
print(i)

produtos_max = produtos[i]
print(produtos_max)

m = vendas.index(menos_vendido)
produtos_min = produtos[m]

print('O produto: {} teve mais produtos vendidos: {} e o produto {} teve menos produtos vendidos: {}'.format(produtos_max, mais_vendido, produtos_min, menos_vendido))