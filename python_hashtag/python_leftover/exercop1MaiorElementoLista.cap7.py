# Exercício 1 - Maior elemento de uma lista
# Escreva a função maior_elemento que recebe como parâmetro uma lista com números inteiros e devolve 
# um número inteiro correspondente ao maior valor presente na lista recebida.

lista = [1 ,2, 1 , 3, 3, 3, 4]

def maior_elemento(lista):
    maior = lista[0] #Atribuimos a variável maior o valor do primeiro elemento da lista (lista[0]).
    for elemento in lista:
        if elemento > maior:
            maior = elemento
    return maior

print(maior_elemento(lista))

#for percorre a lista procurando o maior elemento