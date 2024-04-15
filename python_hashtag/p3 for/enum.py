
##
funcionarios = ['Maria', 'JOse', 'marcio', 'gilberto']
for i, funcionario in enumerate(funcionarios):
    print(i, funcionario)

estoque = [14, 20000, 20, 40000, 20000]
produtos = ['coca', 'pizza', 'cheese', 'sprite', 'guarana']

nivel_minimo = 50
##i =  indice
for i, qtde in enumerate(estoque):
    if qtde < nivel_minimo:
        print('Temos no estoque {} do produto {}'.format(qtde, produtos[i]))