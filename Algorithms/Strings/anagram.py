for test_case in range(int(input())):
    given_string = input()

    if len(given_string) % 2 == 1:
        print(-1)
        continue

    middle = len(given_string) // 2

    left_side = given_string[:middle]
    right_side = list(given_string[middle:])

    for char in left_side:
        if char in right_side:
            right_side.remove(char)

    print(len(right_side))
