n = int(input())
sequence = list(map(int, input().split()))

result = []

for i in range(1, len(sequence) + 1):
    element = sequence.index(i) + 1
    result.append(sequence.index(element) + 1)

for x in result:
    print(x)
