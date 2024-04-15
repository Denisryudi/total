import numpy as np

# random.default_rng() as rng, max, min, mean, argmin, argmax, median, percentile, std, var
rng = np.random.default_rng(seed=42)

dados_vendas = rng.integers(low=50, high=200, size=30)

print(dados_vendas)

print('max', np.max(dados_vendas))

print('item max:', np.argmax(dados_vendas) + 1)

print('min', np.min(dados_vendas))

print('item max:', np.argmin(dados_vendas) + 1)

print('media=', np.mean(dados_vendas))
print('mediana=', np.median(dados_vendas))
print('percentil=', np.percentile(dados_vendas, 25))
print('desvio padrao=', np.std(dados_vendas))
print('variância(quadrado do desvio padrao=', np.var(dados_vendas))
