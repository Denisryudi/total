vendas = [100, 123, 204, 123, 204, 123, 204, 123]

meta = 100

for venda in vendas:
    if venda <= meta:
        print('Não ganha bonus')
        break
    print(venda)



for venda in vendas:
    if venda <= meta:
        print('Não ganha bonus')
        continue
        #pula direto pro próximo - 150. break sai do for, continue pula para o próximo item do for.
    print(venda)