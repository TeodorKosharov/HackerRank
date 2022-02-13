n = int(input())
numbers = list(map(int, input().split()))
print(all(x > 0 for x in numbers) and any(x for x in map(str, numbers) if x == x[::-1]))
