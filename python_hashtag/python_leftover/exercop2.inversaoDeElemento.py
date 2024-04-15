# Exercício 2 - Invertendo sequência
# Como pedido na primeira video-aula desta semana, escreva um programa que recebe uma sequência de números inteiros e imprima todos os 
# valores em ordem inversa. A sequência sempre termina pelo número 0. Note que 0 (ZERO) não deve fazer parte da sequência.


numeros = []
numero = int(input("Digite um número: "))

while numero > 0:
    numeros.append(numero)
    numero = int(input("Digite um número: "))

for i in range(len(numeros)-1, -1, -1):
    print(numeros[i])


# O parâmetro range(len(numeros)-1, -1, -1) define um intervalo que começa no índice do ultimo 
# elemento da lista e vai até o índice 0, reduzindo de 1 em 1.