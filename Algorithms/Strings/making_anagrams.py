first_str = input()
second_str = input()


def number_needed(a, b):
    a_string = [0] * 26

    for ch in a:
        a_string[ord(ch) - 97] += 1

    b_string = [0] * 26
    for ch in b:
        b_string[ord(ch) - 97] += 1

    deletions = 0
    for i in range(len(a_string)):
        deletions += abs(a_string[i] - b_string[i])

    return int(deletions)


print(number_needed(first_str, second_str))
