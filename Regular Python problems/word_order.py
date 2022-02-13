import collections

dictionary = collections.OrderedDict()

for _ in range(int(input())):
    curr_word = input()

    if curr_word not in dictionary:
        dictionary.update({curr_word: 1})
    else:
        dictionary[curr_word] += 1

print(len(dictionary))
print(*dictionary.values())
