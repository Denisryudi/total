meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]
##como precisa do indice de ambos, recomendado usar o enumerate
for venda in vendas:
    if venda[1] >= meta:
        print('Bateram a meta {}, e foi vendido R${:.2f}'.format(venda[0], venda[1]))
