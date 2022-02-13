steps = int(input())
path = input()

position = 0
reached_times_sea_level = 0

for state in path:
    if state == 'D':
        position -= 1

    elif state == 'U':
        position += 1

    if position == 0 and state == 'U':
        reached_times_sea_level += 1

print(reached_times_sea_level)
