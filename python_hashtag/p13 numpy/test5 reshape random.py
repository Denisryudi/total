import numpy as np

rng = np.random.default_rng(seed=1)
vendas_semanais = rng.integers(low=20, high=200, size=(5, 6), endpoint=True)

#vendas_reshape = np.reshape(vendas, (5, 6))
#vendas_reshape1 = np.reshape(vendas, (-1, 6)) #numpy faz o calculo
vendas_total_semana = vendas_semanais.sum(axis=1)
print(vendas_total_semana)
vendas_media_semana = vendas_semanais.mean(axis=1)
print(vendas_media_semana)

vendas_total_dia = vendas_semanais.mean(axis=0)
print(vendas_total_dia)