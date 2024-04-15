# 3 -> [1, 1]

def fibonacci(num):
    if num < 0:
        raise Exception('Num need to be a positive integer')

    res = []
    prev, curr = 1, 1

    for i in range(num):
        res.append(curr)
        #curr + prev = curr2. prev = curr1
        curr, prev = curr + prev, curr

    print(res)
    return res

fibonacci(5)