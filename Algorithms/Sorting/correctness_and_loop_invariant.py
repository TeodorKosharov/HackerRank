n = int(input())
arr = [int(x) for x in input().split()]

is_sorted = False

while not is_sorted:
    for index in range(len(arr) - 1):
        if arr[index] > arr[index + 1]:
            arr[index], arr[index + 1] = arr[index + 1], arr[index]
            break
    else:
        is_sorted = True

print(*arr)
