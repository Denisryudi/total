'''Segunda versão da lista de compras

Mude o programa de lista de compras para usar um dicionário ao invés de uma lista.
O programa deve ter as mesmas funcionalidades, mas agora deve ser possível
adicionar mais de uma unidade de um item na lista de compras. Ou seja, o dicionário
deve armazenar o nome do item e a quantidade desejada pelo usuário. Por exemplo,
se o usuário digitar "banana" e "2", o dicionário deve armazenar "banana" como chave
e 2 como valor. A estrutura do dicionário ficaria assim: `{"banana": 2}`.

O programa deve permitir que o usuário adicione, remova e visualize o dicionário de compras.

Além disso, o programa deve mostrar uma mensagem de erro se o usuário tentar
usar uma opção inválida do menu. Por exemplo, se o usuário digitar 5, o programa
deve mostrar a mensagem "Opção inválida. Por favor, escolha uma opção válida." e
mostrar o menu novamente. Além disso, o programa deve ser *case insensitive*, ou seja,
"Maçã" e "maçã" devem ser considerados o mesmo item.
'''


lista_compras = {}

while True:
    print()

    print('1 Para Adicionar item')
    print('2 Para Remover item')
    print('3 Para Ver a lista')
    print('4 Para sair')

    opcao = input('Digite uma das opções: ')
    if opcao == '1':
        item = input('Digite o nome do item: ')
        quantidade = int(input(''))
        if item in lista_compras:
            lista_compras[item] += quantidade
        else:
            lista_compras[item] = quantidade
    elif opcao == '2':
        item = input('Digite o nome do item: ')
        if item in lista_compras:
            quantidade = int(input('Digite a quantidade: '))
            if quantidade >= item:
                del lista_compras[item]
            else:
                lista_compras[item] -= quantidade
        else:
            print('Item não esta na lista')
    elif opcao == '3':
        for item, quantidade in lista_compras.items():
            print('{} - {}'.format(item, quantidade))
    elif opcao == '4':
        break
