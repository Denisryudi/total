'''### Primeira versão da lista de compras
#%% md
Escreva um programa que permita que um usuário crie uma lista de compras.
O usuário deve ser capaz de adicionar itens, remover itens e visualizar a lista.

Estruture seu programa da seguinte forma:

1. Crie uma lista vazia para armazenar os itens da lista de compras.
2. Crie um loop infinito que imprima um menu de opções ao usuário e permita que ele escolha uma opção.
3. Dentro do loop, use uma declaração if para executar a tarefa apropriada de acordo com a escolha do usuário.
4. Se o usuário escolher adicionar um item, solicite que ele digite o nome do item e adicione-o à lista.
5. Se o usuário escolher remover um item, solicite que ele digite o nome do item e remova-o da lista.
6. Se o usuário escolher ver a lista, mostre cada item da lista em sua própria linha.
7. Se o usuário escolher sair, encerre o loop usando break.
'''


lista_compras = []

while True:
    print()

    print('1 Para Adicionar item')
    print('2 Para Remover item')
    print('3 Para Ver a lista')
    print('4 Para sair')

    opcao = input('Digite uma das opções: ')
    if opcao == '1':
        item = input('Digite o nome do item: ')
        lista_compras.append(item)
    elif opcao == '2':
        item = input('Digite o nome do item: ')
        lista_compras.remove(item)
    elif opcao == '3':
        print(lista_compras)
    elif opcao == '4':
        break
print(lista_compras)
