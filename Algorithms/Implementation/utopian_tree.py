for test_case in range(int(input())):
    height = 1
    cycles = int(input())

    if cycles == 0:
        print(1)
        continue
    else:
        for i in range(cycles):
            if i % 2 == 1:
                height += 1
            else:
                height *= 2

    print(height)
