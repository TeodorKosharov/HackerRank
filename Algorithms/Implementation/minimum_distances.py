n = int(input())
integers = [int(x) for x in input().split()]

distances = []

for index in range(len(integers) - 1):
    current_number = integers[index]
    if current_number in integers[index + 1:]:
        next_number_index = integers[index + 1:].index(current_number)
        distances.append(next_number_index + 1)

print(min(distances) if distances else -1)
