n = int(input())
numbers = list(map(int, input().split()))

print(f'{len([x for x in numbers if x > 0]) / len(numbers):.6f}')
print(f'{len([x for x in numbers if x < 0]) / len(numbers):.6f}')
print(f'{len([x for x in numbers if x == 0]) / len(numbers):.6f}')
