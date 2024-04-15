import numpy as np

vendas = np.array([[50, 60, 70, 65, 80],
                   [85, 90, 78, 92, 88],
                   [72, 75, 68, 77, 76]])

vendas_por_produto = vendas.sum(axis=1)
#ou np.sum(vendas, axis=1)
print(vendas_por_produto)

vendas_por_dia = vendas.sum(axis=0)