n, k = map(int, input().split())
arr = list(map(int, input().split()))

valid_pairs = 0
for first_index in range(len(arr)):
    for second_index in range(first_index, len(arr)):
        if first_index < second_index and (arr[first_index] + arr[second_index]) % k == 0:
            valid_pairs += 1

print(valid_pairs)
