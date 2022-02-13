n = int(input())
arr = list(map(int, input().split()))

max_points = max(arr)
arr = [item for item in arr if item < max_points]
print(max(arr))
