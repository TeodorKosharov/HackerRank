def wrap(string, max_width):
    res = ''
    while len(string) > 0:
        res += string[0: max_width] + '\n'
        string = string[max_width:]
    return res


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
