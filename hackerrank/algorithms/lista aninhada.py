if __name__ == '__main__':
    records = []
    for i, _ in enumerate(range(int(input()))):
        name = input()
        score = float(input())
        records.append([name, score])
    ordered_records = sorted(records, key=lambda x: (x[1], x[0]))


    # Find the second lowest score
    lowest_score = ordered_records[0][1]
    second_lowest_score = None
    #    substituicao lowest_score vira o score
    for name, score in ordered_records:
        if score > lowest_score:
            second_lowest_score = score
            break

    for name, score in ordered_records:
        if score == second_lowest_score:
            print(name)

#gpt


if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    # Sort records by score, then by name
    ordered_records = sorted(records, key=lambda x: (x[1], x[0]))

    # Find the second lowest score
    lowest_score = ordered_records[0][1]
    second_lowest_score = None
    for name, score in ordered_records:
        if score > lowest_score:
            second_lowest_score = score
            break

    # Print names of students with the second lowest score
    for name, score in ordered_records:
        if score == second_lowest_score:
            print(name)