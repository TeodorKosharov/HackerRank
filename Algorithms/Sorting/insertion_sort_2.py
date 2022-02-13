n = int(input())
arr = [int(x) for x in input().split()]

for element_index in range(1, n):
    end_index = element_index - 1

    for index in range(end_index + 1):
        if arr[element_index] < arr[index]:
            arr[element_index], arr[index] = arr[index], arr[element_index]
    print(*arr)
