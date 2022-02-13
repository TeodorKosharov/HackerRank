for query in range(int(input())):
    given_string = input()
    reversed_string = given_string[::-1]

    for index in range(len(given_string) - 1):
        if abs(ord(given_string[index]) - ord(given_string[index + 1])) != \
                abs(ord(reversed_string[index]) - ord(reversed_string[index + 1])):
            print('Not Funny')
            break
    else:
        print('Funny')
