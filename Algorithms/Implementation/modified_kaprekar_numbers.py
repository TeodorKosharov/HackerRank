start, end = (int(input()) for _ in range(2))

result = []
if start == 1:
    result.append(1)

for num in range(start, end + 1):
    squared_num = num ** 2
    if len(str(squared_num)) >= 2:
        middle = len(str(squared_num)) // 2

        if int(str(squared_num)[:middle]) + int(str(squared_num)[middle:]) == num:
            result.append(num)

if result:
    print(*result)
else:
    print('INVALID RANGE')
