# Exercício 1 - Removendo elementos repetidos
# Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal lista possui elementos repetidos e 
# os remove. A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.

# Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?

# >>>lista = [2, 4, 2, 2, 3, 3, 1]
# >>>remove_repetidos(lista)
# [1, 2, 3, 4]
# >>>remove_repetidos([1, 2, 3, 3, 3, 4])
# [1, 2, 3, 4]
# lista = [1 ,2, 1 , 3, 3, 3, 4]

# def remove_repetidos(lista):
#     lista_sem_repetidos = list(set(lista))
    
#     return lista_sem_repetidos
# print(lista)

# r= [1, 2, 1, 3, 3, 3, 4]

lista = [1 ,2, 1 , 3, 3, 3, 4]

def remove_repetidos(lista):
    lista_sem_repetidos = list(set(lista))
    lista_sem_repetidos.sort() #deixa em ordem
    return lista_sem_repetidos
print(lista)
