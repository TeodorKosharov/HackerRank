starting_people = 2
result = 2

for case in range(int(input()) - 1):
    starting_people *= 3
    starting_people //= 2
    result += starting_people

print(result)
