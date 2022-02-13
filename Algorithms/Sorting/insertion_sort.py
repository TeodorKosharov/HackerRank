n = int(input())
arr = [int(x) for x in input().split()]

last_el = arr[-1]

for index in range(1, len(arr) + 1):
    if -index > -len(arr) and last_el < arr[-index - 1]:
        arr[-index] = arr[-index - 1]
        print(*arr)
    else:
        arr[-index] = last_el
        print(*arr)
        break
