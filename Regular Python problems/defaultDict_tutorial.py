# from collections import defaultdict
#
# n, m = list(map(int, input().split()))
# d = defaultdict(list)
# for i in range(n):
#     d[input()].append(i + 1)
# for i in range(m):
#     print(*d[input()] or [-1])

import collections

n, m = input().split()
dictionary = collections.defaultdict(list)

for i in range(1, int(n) + 1):
    dictionary[input()].append(i)

for x in range(int(m)):
    check_value = input()
    if check_value in dictionary:
        print(*dictionary[check_value])
    else:
        print(-1)
