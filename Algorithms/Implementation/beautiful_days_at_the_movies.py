i, j, k = map(int, input().split())

beautiful_days = 0
for day in range(i, j + 1):
    day = str(day)
    if (int(day) - int(day[::-1])) % k == 0:
        beautiful_days += 1

print(beautiful_days)
