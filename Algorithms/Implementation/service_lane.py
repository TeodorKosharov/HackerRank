n, t = [int(x) for x in input().split()]
width = [int(x) for x in input().split()]

for case in range(t):
    coordinates = [int(x) for x in input().split()]
    print(min(width[coordinates[0]: coordinates[1] + 1]))
