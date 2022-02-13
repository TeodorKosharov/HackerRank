given_string = input()
unique_chars = set(given_string)

if len(given_string) % 2 == 0:
    if len([x for x in unique_chars if given_string.count(x) % 2 == 0]) == len(unique_chars):
        print('YES')
    else:
        print('NO')
else:
    evens = [x for x in unique_chars if given_string.count(x) % 2 == 0]
    odds = [x for x in unique_chars if given_string.count(x) % 2 == 1]

    if abs(len(evens) - len(odds)) == 1 or len(evens) == len(odds):
        print('YES')
    else:
        print('NO')
