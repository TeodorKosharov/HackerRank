from math import sqrt, floor, ceil

encrypted_word = input().replace(' ', '')

min_value = floor(sqrt(len(encrypted_word)))
max_value = ceil(sqrt(len(encrypted_word)))

start = 0
for i in range(max_value):
    res = ''
    for index in range(start, len(encrypted_word), max_value):
        res += encrypted_word[index]
    start += 1
    print(res, end=' ')
