# First variant:

# word = input()
#
# lowers = ''
# uppers = ''
# evens = ''
# odds = ''
#
# for char in word:
#     if char.islower():
#         lowers += char
#     elif char.isupper():
#         uppers += char
#     elif int(char) % 2 == 0:
#         evens += char
#     elif int(char) % 2 == 1:
#         odds += char
#
# print(''.join(sorted(lowers) + sorted(uppers) + sorted(odds) + sorted(evens)))


# Second variant:

# word = input()
# lowers, uppers, odds, evens = [], [], [], []
# for char in sorted(word):
#     if char.isalpha():
#         x = uppers if char.isupper() else lowers
#     else:
#         x = evens if int(char) % 2 == 0 else odds
#     x.append(char)
# print(''.join(lowers + uppers + odds + evens))


# Third variant:

word = sorted(input())

lowers = [x for x in word if x.islower()]
uppers = [x for x in word if x.isupper()]
odds = [x for x in [int(y) for y in word if y.isdigit()] if x % 2 == 1]
evens = [x for x in [int(y) for y in word if y.isdigit()] if x % 2 == 0]

print(''.join(lowers + uppers + list(map(str, odds)) + list(map(str, evens))))
