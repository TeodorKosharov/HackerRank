# n = int(input())
# arr = [int(x) for x in input().split()]
#
# elements_dict = {}
#
# for num in arr:
#     if num not in elements_dict:
#         elements_dict[num] = 0
#     elements_dict[num] += 1
#
# # using zip function to extract the key with the maximum value
# most_frequent_value = max(zip(elements_dict.values(), elements_dict.keys()))[1]
# print(len(arr) - len([x for x in arr if x == most_frequent_value]))


# Second variant:

n = int(input())
arr = [int(x) for x in input().split()]

elements_dict = {}

for num in arr:
    if num not in elements_dict:
        elements_dict[num] = 0
    elements_dict[num] += 1

# using comprehension to extract the key with the maximum value
most_frequent_value = max(elements_dict.values())
max_element = [x for x in elements_dict.keys() if elements_dict[x] == most_frequent_value][0]

print(len(arr) - len([x for x in arr if x == max_element]))
