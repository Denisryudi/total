venda = input('Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter com a caixa vazia')
vendas = []

while venda != '':
    vendas.append(venda)
    print('Registro Finalizado. As vendas cadastradas foram: {}'.format(vendas))

print(vendas)