import time

tempo_atual = time.localtime()
tempo_ano_novo = time.mktime((2024, 1, 29, 0, 0, 0, 0, 0, 0))

print(tempo_atual)
print(tempo_ano_novo)
diferenca = time.mktime(tempo_atual) - tempo_ano_novo
print(f"Diferença em segundos: {diferenca}")