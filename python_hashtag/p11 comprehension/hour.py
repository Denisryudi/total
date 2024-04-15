

soma = 0
for i in range(3):
    for j in range(3):
        somar = (i, j) + (i, j+1) + (i, j+2) + (i+1, j+1) +(i+2, j) +(i+2, j+1)+(i+2, j+2)
        soma += sum(somar)
print(soma)

max_sum = -63  # minimum possible hourglass sum (-9 * 7)

#or i in range(4):
    #or j in range(4):
 #      current_sum = sum(arr[i][j:j + 3]) + arr[i + 1][j + 1] + sum(arr[i + 2][j:j + 3])
     #  max_sum = max(max_sum, current_sum)

#rturn max_sum
