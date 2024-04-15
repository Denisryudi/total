produtos = ['coca', 'pizza', 'cheese', 'sprite', 'guarana']
producao = ['15000', '20000', '30000', '40000', '20000']

tamanho = len(produtos)
for i in range(tamanho):
    print('Temos {} na quantidade de {} '.format(produtos[i], producao[i]))

##ou



for i in range(len(produtos)):
    print('------Temos {} na quantidade de {} '.format(produtos[i], producao[i]))

produtos1 = ['coca', 'pizza', 'cheese', 'sprite', 'guarana']
producao1 = ['15000', '20000', '30000', '40000', '20000']


for j in range(len(produtos1)):
    produto2 = produtos1[j]
    producao2 = producao1[j]
    print(produto2, producao2)