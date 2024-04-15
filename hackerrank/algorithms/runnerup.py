if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_list = list(arr)

    arr_list_sorted = sorted(arr_list)
    print('lista ordenada crua{}'.format(arr_list_sorted))
    #remove duplicados
    unique_sorted_numbers = list(dict.fromkeys(arr_list_sorted))
    vice_list = unique_sorted_numbers[:-1]
    vice_list_max = max(vice_list)
    print(vice_list_max)




#chatgpt abaixo

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_list = list(arr)

    # Agora arr_list é uma lista de inteiros. Podemos ordená-la diretamente.
    arr_list_sorted = sorted(arr_list)

    # Removendo duplicatas e o maior número (se for isso que você deseja)
    unique_sorted_numbers = list(dict.fromkeys(arr_list_sorted))  # Remove duplicatas
    unique_sorted_numbers.remove(max(unique_sorted_numbers))  # Remove o maior número

    print(unique_sorted_numbers)

