preco_produtos = [100, 150, 300, 5500]
produtos = ['vinho', 'cafeteira', 'microondas', 'iphone']

preco_impostos = []

for i, item in enumerate(preco_produtos):
    preco_impostos.append(item*0.3)

    print('Ficou com imposto:{} do produto:{}'.format(preco_impostos, produtos[i]))


print('Com list comprehension:')

impostos = [preco * 0.3 for preco in preco_produtos]
print(impostos)

def calcular_imposto(preco, imposto):
    return preco * imposto

impostos = [calcular_imposto(preco, 0.3) for preco in preco_produtos]