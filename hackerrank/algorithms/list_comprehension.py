
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
        #lista com essas cordenadas
        #obs: x+1 = inclusive
    juncao_total = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]

    print(juncao_total)