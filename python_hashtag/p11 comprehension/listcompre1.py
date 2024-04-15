preco_produtos = [100, 150, 300, 5500]
produtos = ['vinho', 'cafeteira', 'microondas', 'iphone']

lista_aux = list(zip(preco_produtos, produtos))
lista_aux.sort(reverse=True)
produtos = [produto for preco, produto in lista_aux]
print(lista_aux)