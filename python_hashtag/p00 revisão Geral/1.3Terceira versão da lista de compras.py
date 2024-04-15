'''
Mantenha o programa da lista de compras com dicionário, mas agora use funções para organizar o código.
Crie funções para cada uma das opções do menu: `adicionar_item`, `remover_item` e
`ver_lista`. Crie também uma função para mostrar o menu. O programa deve continuar
funcionando da mesma forma, mas agora o código deve estar organizado em funções.
'''


def adicionar_item(lista_compras):
    item = input('Digite o nome do item: ')
    quantidade = int(input(''))
    if item in lista_compras:
        lista_compras[item] += quantidade
    else:
        lista_compras[item] = quantidade


def remover_item(lista_compras):
    item = input('Digite o nome do item: ')
    if item in lista_compras:
        quantidade = int(input('Digite a quantidade: '))
        if quantidade >= lista_compras[item]:
            del lista_compras[item]
        else:
            lista_compras[item] -= quantidade
    else:
        print('Item não esta na lista')


def ver_lista(lista_compras):
    for item, quantidade in lista_compras.items():
        print('{} - {}'.format(item, quantidade))


def main():
    lista_compras = {}
    while True:
        print()

        print('1 Para Adicionar item')
        print('2 Para Remover item')
        print('3 Para Ver a lista')
        print('4 Para sair')
        opcao = input('Digite a sua escolha: ')

        if opcao == '1':
            adicionar_item(lista_compras)
        elif opcao == '2':
            remover_item(lista_compras)
        elif opcao == '3':
            ver_lista(lista_compras)
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
