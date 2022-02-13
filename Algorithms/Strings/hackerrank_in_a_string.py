from collections import deque

for _ in range(int(input())):
    sample = deque('hackerrank')
    word = input()

    for char in word:
        if sample and char == sample[0]:
            sample.popleft()

    if sample:
        print('NO')
    else:
        print('YES')
