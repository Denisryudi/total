def simpleArraySum(ar):
    sum(ar)


# Example usage:
ar = [1, 2, 3, 4, 10, 11]
print(simpleArraySum(ar))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
