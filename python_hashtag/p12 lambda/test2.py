def calcular_imposto(imposto):
    # lambda um construtor de função
    #lambda recebe como parâmetro o imposto, e com ela retorna uma função que recebe como
# parâmetro o preco e me da como resposta o preço*imposto
    return lambda preco: preco * (1+ imposto)

calcular_preco_produto = calcular_imposto(0.1)
calcular_preco_servico = calcular_imposto(0.15)
calcular_preco_royalties = calcular_imposto(3)

print(calcular_preco_produto(100))
