for test_case in range(int(input())):

    number = input()
    divisors = 0

    for digit in number:
        if int(digit) != 0 and int(number) % int(digit) == 0:
            divisors += 1

    print(divisors)
