preco_tecnologia = {'notebook asus': 2450, 'iphone': 4500, 'samsung galaxy': 3000, 'tv samsung': 1000, 'ps5': 3000, 'tablet': 1000, 'notebook dell': 3000, 'ipad': 3000, 'tv philco': 800, 'notebook hp': 1700}

preco_com_imposto = list(map(lambda preco: preco * 1.3, preco_tecnologia.values()))
print(preco_com_imposto)


produtos_acima2000 = dict(list(filter(lambda preco1: preco1[1] > 2000, preco_tecnologia.items())))
#saida dict
print(produtos_acima2000)