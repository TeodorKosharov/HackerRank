for query in range(int(input())):
    given_string = input()

    operations = 0
    for index in range(len(given_string) // 2):
        if given_string[index] != given_string[-1 - index]:
            operations += abs(ord(given_string[index]) - ord(given_string[-1 - index]))

    print(operations)
