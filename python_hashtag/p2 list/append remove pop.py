produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
print(produtos)

produtos[2] = 'mortadela'
produtos.append('iphone 11')
print(produtos)

produtos.remove('mouse')
print(produtos)

item_removido = produtos.pop(0)
print(produtos)
print('Removemos o item: {} da lista'.format(item_removido))

#remover teclado

teclado_remover = 'tecladoo'

if teclado_remover in produtos:                     #<----------1ª in
    produtos.remove('tecladoo')
else:
    print('{} não existe na lista de produtos'.format(teclado_remover))
    print(produtos)
    
    print('!!!!!!!!!!!!!!!')
    
try:                                                #<----------2ª try
    produtos.remove('tecladoo')
except:
    print('tecladoo não existe na lista de produtos')
    
print('!@!@!@!@!@!')

try:
    produtos.remove('tecladoo')
    print(produtos)
except:
    pass


