# First variant:

# def solve(s):
#     res = s[0].upper()
#     is_last_char_space = False
#     for index in range(1, len(s)):
#
#         if s[index].isalpha() and is_last_char_space:
#             res += s[index].upper()
#         else:
#             res += s[index]
#
#         if s[index] == ' ':
#             is_last_char_space = True
#         else:
#             is_last_char_space = False
#
#     return res


# Efficient variant:

def solve(s):
    s = s.split(' ')
    return ' '.join(x.capitalize() for x in s)


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
