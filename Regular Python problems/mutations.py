def mutate_string(string, position, character):
    # First variant:
    # return string[:position] + character + string[position + 1:]

    # Second variant:
    string = list(string)
    string[position] = character
    return ''.join(string)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
