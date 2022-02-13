n = int(input())
arr = [int(x) for x in input().split()]

arr.sort()
print(arr[len(arr) // 2])
