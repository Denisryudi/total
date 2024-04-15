'''Escreva um programa que calcula o total e a média de vendas para cada vendedor em uma empresa. O usuário deve digitar o nome do vendedor
e suas vendas, e o programa deve manter o controle do total e da média de vendas para cada vendedor.
Estruture seu programa da seguinte forma:
Crie um dicionário vazio para armazenar os dados de vendas.
Crie um loop infinito que solicite ao usuário o nome do vendedor e suas vendas.
Dentro do loop, use uma declaração if para verificar se o usuário digitou ‘sair’.
Se o usuário digitar ‘sair’, encerre o loop usando break.
Se o usuário digitar qualquer outra coisa, use as entradas para calcular o total e a média de vendas para o vendedor e adicione-os ao dicionário.
Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar o total e a média de vendas para cada vendedor.
'''

dados_vendas = {}

while True:
    print('Digite o nome do vendedor, ou ''sair'' para finalizar o app')
    nome_vendedor = input('Digite o nome do vendedor: ')
    if nome_vendedor.lower() == 'sair':
        break
    qtde_vendas = int(input('Digite a quantidade de vendas: '))
    total_vendas = int(input('Digite o total de vendas: '))
    media_vendas = total_vendas/qtde_vendas
    dados_vendas[nome_vendedor] = media_vendas

    for nome_vendedor, media_vendas in dados_vendas.items():
        print('A média de vendas foi de {} para o vendedor: {}.'.format(nome_vendedor, media_vendas))


