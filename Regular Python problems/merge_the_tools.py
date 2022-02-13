# First variant:

# def merge_the_tools(string, k):
#     res = ''
#     while len(string) > 0:
#         unique_chars = []
#         for char in string[0:k]:
#             if char not in unique_chars:
#                 unique_chars.append(char)
#
#         res += ''.join(unique_chars) + '\n'
#         string = string[k:]
#
#     print(res)


# Second variant:

def merge_the_tools(string, k):
    res = ''
    n = 0
    temp = k
    for _ in range(len(string)):
        unique_chars = []
        for char in string[n:k]:
            if char not in unique_chars:
                unique_chars.append(char)

        res += ''.join(unique_chars) + '\n'
        n += temp
        k += temp

    print(res)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
