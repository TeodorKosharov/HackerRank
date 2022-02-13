n = int(input())
numbers = list(map(int, input().split()))

maximum = 0
for num in numbers:
    a = numbers.count(num)
    b = numbers.count(num - 1)
    res = a + b

    if res > maximum:
        maximum = res

print(maximum)
