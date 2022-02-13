n, m = map(int, input().split())
rows = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

rows = sorted(rows, key=lambda x: x[k])
for i in rows:
    print(*i)
