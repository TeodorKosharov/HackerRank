# for case in range(int(input())):
#     str1 = input()
#     str2 = input()
#
#     if any([True for x in str1 if x in str2]):
#         print('YES')
#     else:
#         print('NO')


# Second approach:

for case in range(int(input())):
    str1 = input()
    str2 = input()

    print('YES' if set(str1).intersection(set(str2)) else 'NO')
    # print('YES' if set(str1) & set(str2) else 'NO')
