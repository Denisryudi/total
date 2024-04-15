produtos = ['tv', 'Celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
novos_produtos = ['handphone', 'thunderstone']

tv_vermelha_unidades = [15000]
tv_vermelha = 'vermelha'

tv_verde_unidades = [54545]
tv_azul_unidades = [21233]

produtos.extend(novos_produtos)
print(produtos)

total_tv_vermelha = str(tv_vermelha_unidades) + tv_vermelha #possivel transformar um int em str, mas não um str em int
print(total_tv_vermelha) #[15000]vermelha

tv_azul_unidades.extend(tv_vermelha) 
print(tv_azul_unidades) #[21233, 'v', 'e', 'r', 'm', 'e', 'l', 'h', 'a']


tv_vermelha_unidades.extend(tv_verde_unidades)
print(tv_vermelha_unidades) #[15000, 54545]


total_azul_verde = tv_azul_unidades[0] + tv_verde_unidades[0]
print(total_azul_verde)
print('#@!@!@!@!@!@!')
vendas = [100, 150, 100, 120, 70, 90, 80]

produtos.sort()
vendas.sort()
print(vendas, produtos)

vendas.sort(reverse=True) #decrecente, perde a ordenação da lista (relacionamento entre listas)
print(vendas)

