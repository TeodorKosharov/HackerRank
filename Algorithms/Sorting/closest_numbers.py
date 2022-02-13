# from sys import maxsize
#
# n = int(input())
# arr = [int(x) for x in input().split()]
#
# closest_nums = {}
# min_diff = maxsize
# pairs = []
#
# while arr:
#     is_min_diff_updated = False
#     max_num1 = max(arr)
#     arr = [x for x in arr if x != max_num1]
#
#     if not arr:
#         break
#
#     max_num2 = max(arr)
#
#     diff = abs(max_num1 - max_num2)
#     if diff <= min_diff:
#         min_diff = diff
#
#         if max_num1 < max_num2:
#             pair = max_num1, max_num2
#         else:
#             pair = max_num2, max_num1
#
#         if pair not in pairs:
#             is_min_diff_updated = True
#
#         pairs.append((max_num1, max_num2))
#         pairs.append((max_num2, max_num1))
#
#         if is_min_diff_updated:
#             closest_nums[(pair[0], pair[1])] = min_diff
#
# min_diff = closest_nums[min(closest_nums, key=lambda x: x[1])]
# min_diff_pairs = {p: d for p, d in closest_nums.items() if d == min_diff}
#
# for pair in sorted(min_diff_pairs):
#     print(f'{pair[0]} {pair[1]}', end=' ')


# Better approach:

n = input()
nums = list(map(int, input().strip().split()))
nums.sort()
min_diff = nums[1] - nums[0]
res = [nums[0], nums[1]]

for i in range(1, len(nums) - 1):

    if nums[i + 1] - nums[i] < min_diff:
        res = []
        res.append(nums[i])
        res.append(nums[i + 1])
        min_diff = abs(nums[i + 1] - nums[i])

    elif nums[i + 1] - nums[i] == min_diff:
        res.append(nums[i])
        res.append(nums[i + 1])

print(*res)
