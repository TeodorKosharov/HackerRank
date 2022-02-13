n, k, q = map(int, input().split())
numbers = list(map(int, input().split()))

queries = []
for _ in range(q):
    queries.append(int(input()))

for rotation in range(k):
    numbers.insert(0, numbers.pop(-1))  # We remove the element at the last index and then insert it at 0 index

for index in queries:
    print(numbers[index])
