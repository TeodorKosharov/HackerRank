# from string import ascii_lowercase
# from collections import deque
#
# alphabet_letters = deque(ascii_lowercase)
# given_string = sorted(input().lower())
#
# for char in given_string:
#
#     if not alphabet_letters:
#         print('pangram')
#         exit(0)
#
#     if char == alphabet_letters[0]:
#         alphabet_letters.popleft()
#
# if alphabet_letters:
#     print('not pangram')
# else:
#     print('pangram')

# Second approach:
from string import ascii_lowercase

given_string = input().lower()
given_string = set(given_string.replace(' ', ''))


if len(given_string) >= len(ascii_lowercase):
    print('pangram')
else:
    print('not pangram')
