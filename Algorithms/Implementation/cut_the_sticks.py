n = int(input())
sticks = list(map(int, input().split()))

result = []

while sticks:
    min_stick = min(sticks)
    result.append(len(sticks))

    for stick_index in range(len(sticks)):
        sticks[stick_index] -= min_stick

    sticks = [x for x in sticks if x > 0]

print(*result, sep='\n')
