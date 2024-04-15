#i = lista.index('item')

produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
estoque = [100, 150, 100, 120, 70, 90, 80]


#i = produtos.index('geladeira')
#qtde_estoque = estoque[i]
#print(qtde_estoque)


print(produtos)

nomeProduto = input('Insira o nome do produto')
i = produtos.index(nomeProduto)
print(i)
if(nomeProduto):
    print('Produto {} tem no estoque: {} desse produto.'.format(produtos[i],estoque[i]))
else:
    print('Não existe esse produto na lista.')
    