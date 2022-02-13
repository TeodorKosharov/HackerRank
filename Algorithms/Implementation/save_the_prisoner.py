for case in range(int(input())):
    prisoners, sweets, starting_chair = map(int, input().split())
    print(((starting_chair - 1 + sweets - 1) % prisoners) + 1)
