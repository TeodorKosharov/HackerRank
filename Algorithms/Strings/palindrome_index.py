def is_palindrome(word):
    for index in range(len(word) // 2):
        if word[index] != word[-1 - index]:
            return False
    return True


for query in range(int(input())):
    given_string = input()

    if is_palindrome(given_string):
        print(-1)
        continue

    given_string = list(given_string)

    for element_index in range(len(given_string)):
        given_string_copy = given_string.copy()
        given_string_copy.pop(element_index)

        if is_palindrome(given_string_copy):
            print(element_index)
            break
    else:
        print(-1)
