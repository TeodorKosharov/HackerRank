def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']

    s = 0
    k = 0
    for i in range(len(string)):
        if string[i] in vowels:
            k += len(string) - i
        else:
            s += len(string) - i

    if s == k:
        print('Draw')
    elif s > k:
        print(f'Stuart {s}')
    else:
        print(f'Kevin {k}')


if __name__ == '__main__':
    s = input()
    minion_game(s)
