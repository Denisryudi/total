
produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
print('\n'.join(produtos))
#tv
#celular
#tablet
#mouse
#teclado
#geladeira
#forno


produtos_str = 'tv, celular, tablet, mouse, teclado, geladeira, forno'

lista = produtos_str.split(', ')
print(lista)



lista1 = ['tv', 'celular']

vendas = [100, 200]

lista1 += ['Ipad']
print(lista1)

soma_vendas = 300
#adicionando na soma a quantidade de Ipad
soma_vendas += 500
print(soma_vendas)

email = 'Esse mês vendemos um total de {} produtos, sendo: \n{} unidades de {}\n{} unidades de {}.'.format(soma_vendas, vendas[0], lista1[0], vendas[1], lista[1])
print(email)

email += '\n{} unidades de Ipad'.format(500)
print(email)