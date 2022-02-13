n = int(input())
arr = [int(x) for x in input().split()]

values = [0] * 100

for index in range(len(arr)):
    values[arr[index]] += 1

index_counter = 0
for occurrences in values:
    for num in range(occurrences):
        print(index_counter, end=' ')

    index_counter += 1
