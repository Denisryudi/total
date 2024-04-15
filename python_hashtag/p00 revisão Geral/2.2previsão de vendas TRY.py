previsao = {}

while True:

        nome = input('Digite o nome do produto (ou ''sair'' para sair)')
        if nome.lower() == 'sair':
            break
        try:
            vendas_mes_atual = float(input('Digite as vendas do mês atual'))
            taxa_crescimento = float(input('Digite a taxa de crescimento (%)'))
        except ValueError:
            print('Entrada inválida, favor digitar um valor para venda e taxa de crescimento.')
            continue

        vendas_proximo_mes = vendas_mes_atual * (1 + taxa_crescimento / 100)
        previsao[nome] = vendas_proximo_mes

        for nome, vendas_proximo_mes in previsao.items():
            print('A previsão de vendas do produto:{}, no próximo mês é de R${:.2f}'.format(nome, vendas_proximo_mes))
