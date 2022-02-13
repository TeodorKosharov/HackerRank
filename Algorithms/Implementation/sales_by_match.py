n = int(input())
socks_colors = map(int, input().split())
colors = {}
pairs = 0

for color in socks_colors:
    if color not in colors:
        colors[color] = 1
    else:
        colors[color] += 1

    if colors[color] == 2:
        pairs += 1
        colors[color] = 0

print(pairs)
