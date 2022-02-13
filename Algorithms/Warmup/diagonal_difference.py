first_diagonal = 0
second_diagonal = 0

for index in range(1, int(input()) + 1):
    line = list(map(int, input().split()))
    first_diagonal += line[index - 1]
    second_diagonal += line[-index]

print(abs(first_diagonal - second_diagonal))
