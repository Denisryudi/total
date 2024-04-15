# Exercício 2 - Soma dos elementos de uma lista
# Escreva a função soma_elementos que recebe como parâmetro uma lista com 
# números inteiros e devolve um número inteiro correspondente à soma dos elementos
# da lista recebida.
lista = [1 ,2, 1 , 3, 3, 3, 4]

def soma_elementos(lista):
    soma = 0
    for elemento in lista:
        soma = soma + elemento
    return soma

print(soma_elementos(lista))

# basicamente foi criado Elemento, e com o for foi possivel adicionar nele a Soma que alterou a sua composição no quesito de agora somar 