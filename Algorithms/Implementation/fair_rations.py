n = int(input())
arr = [int(x) for x in input().split()]

given_bread = 0
index = 0

if len([x for x in arr if x % 2 == 0]) == len([x for x in arr if x % 2 == 1]) \
        or len([x for x in arr if x % 2 == 1]) % 2 == 1:
    print('NO')
    exit()

while not all(True if x % 2 == 0 else False for x in arr):
    if arr[index] % 2 == 1:
        arr[index] += 1
        arr[index + 1] += 1
        given_bread += 2

    index += 1
    if index == len(arr) - 1:
        index = 0

print(given_bread)
