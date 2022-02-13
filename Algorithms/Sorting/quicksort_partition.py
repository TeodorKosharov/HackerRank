n = int(input())
arr = [int(x) for x in input().split()]

left = []
right = []
pivot = arr[0]

left.extend(x for x in arr[1:] if x < pivot)
right.extend(x for x in arr[1:] if x > pivot)

left.append(pivot)
print(*(left + right))
