for i in range(1, int(input()) + 1):
    print(f"{''.join(map(str, [x for x in range(1, i + 1)]))}{''.join(map(str, [y for y in range(i - 1, 0, -1)]))}")

# First we print the nums from 1 to i, then from i - 1 to 1
# example: i = 3  --->  12321
