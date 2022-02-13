n = int(input())
bird_ids = map(int, input().split())

dictionary = {}
for id in bird_ids:
    if id not in dictionary:
        dictionary.update({id: 1})
    else:
        dictionary[id] += 1

# dictionary = dict(sorted(dictionary.items(), key=lambda x: (-x[1], x[0])))
# print(list(dictionary.items())[0][0])


# Second variant - manual algorithm without the help of sortings and helpful methods:

# Finding the bird id's with the most occurrences:
max_value = 0
for value in dictionary.values():
    if value > max_value:
        max_value = value

# New dictionary with only the most occurrences of the specific bird id:
new_dict = {}
for key, value in dictionary.items():
    if value == max_value:
        new_dict.update({key: value})

# Finding the minimum id:
min_key = list(new_dict.items())[0][0]
for key in new_dict.keys():
    if key < min_key:
        min_key = key

print(min_key)
