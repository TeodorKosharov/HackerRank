n = int(input())
chocolate_squares = list(map(int, input().split()))
day, month = list(map(int, input().split()))

counter = 0
index = 0

for _ in range(len(chocolate_squares)):
    if sum(chocolate_squares[index:month]) == day:
        counter += 1
    index += 1
    month += 1

print(counter)
