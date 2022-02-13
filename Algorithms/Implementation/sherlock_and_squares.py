# First variant:
# In the first variant we iterated through all the numbers but this is not very efficient algorythm.

# for test_case in range(int(input())):
#     start, end = map(int, input().split())
#
#     numbers = [int(x) for x in range(start, end + 1) if pow(x, 1 / 2).is_integer()]
#     print(len(numbers))
#


# Efficient variant:
# If we find the square roots of our start and end values, that will give -
# us a start and end of this range of integers which provide the squared values in our required range.

from math import floor, sqrt, ceil

for test_case in range(int(input())):
    start, end = map(int, input().split())
    start = ceil(sqrt(start))
    end = floor(sqrt(end))
    counter = 0
    for i in range(start, end + 1):
        counter += 1
    print(counter)
