for _ in range(int(input())):
    given_string = input()
    middle = len(given_string) // 2
    possible_numbers = []

    for i in range(1):
        for j in range(middle):
            possible_numbers.append(int(given_string[i: j + 1]))

    for starting_number in possible_numbers:
        new_string = ''
        start = starting_number

        while len(new_string) < len(given_string):
            new_string += str(starting_number)
            starting_number = int(starting_number) + 1

        if given_string == new_string:
            print(f'YES {start}')
            break
    else:
        print('NO')
