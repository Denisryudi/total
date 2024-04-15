import numpy as np

salarios = np.array([3000, 3500, 4000, 2000, 4500, 4000, 5000])

media_salarial = np.mean(salarios)
print(media_salarial)

funcionarios_acima_media = np.where(salarios > media_salarial)
print(funcionarios_acima_media)

print(salarios[funcionarios_acima_media])

salarios_bonus = np.where(salarios < media_salarial, salarios * 1.1, salarios)

print(salarios)
print(salarios_bonus)

print(np.where((salarios >= 3000) & (salarios <=4500)))
acima_3000_menor_4500 = np.where((salarios >= 3000) & (salarios <=4500))
print(salarios[acima_3000_menor_4500])


salarios_ajustados = np.where((salarios >= 3000) & (salarios <=4500), salarios * 1.05, salarios)
print(salarios_ajustados)

print(np.where((salarios_ajustados < 3000) | (salarios_ajustados > 4500), salarios * 1.30, salarios_ajustados))
