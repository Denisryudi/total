def padronizar_texto(texto):
    texto = texto.casefold()
    texto = texto.replace("  ", "  ")
    texto = texto.strip()
    return texto


produtos = [' ACB12  ', 'abc43', 'abC37', 'beb12', 'BSA151', 'BEB23']

for i, produto in enumerate(produtos):
    produtos[i] = padronizar_texto(produto)

print(produtos)

produtos = list(map(padronizar_texto, produtos))
print(produtos)

imposto = 90
def preco_imposto1(preco):
    return preco * (1 + 0.3)
print(preco_imposto1(100))

preco_imposto = lambda preco: preco * (1 + imposto)
print(preco_imposto(100))