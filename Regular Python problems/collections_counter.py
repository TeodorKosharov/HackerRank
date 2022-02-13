# number_of_shoes = int(input())
# shoe_sizes = input().split()
#
# profit = 0
#
# for purchase in range(int(input())):
#     purchase_data = input().split()
#     if purchase_data[0] in shoe_sizes:
#         shoe_sizes.remove(purchase_data[0])
#         profit += int(purchase_data[1])
#
# print(profit)

import collections

number_of_shoes = int(input())
shoe_sizes = dict(collections.Counter(input().split()))

profit = 0

for purchase in range(int(input())):
    purchase_data = input().split()
    if purchase_data[0] in shoe_sizes and shoe_sizes[purchase_data[0]] > 0:
        shoe_sizes[purchase_data[0]] -= 1
        profit += int(purchase_data[1])

print(profit)
