# In this challenge, the user enters a string and a substring.
# You have to print the number of times that the substring occurs in the given string.


def count_substring(string, sub_string):
    sub_str_length = len(sub_string)
    string_length = len(string)
    start_index = 0
    counter = 0

    for _ in range(string_length - sub_str_length + 1):
        current_string = string[start_index:sub_str_length]
        start_index += 1
        sub_str_length += 1
        if current_string == sub_string:
            counter += 1

    return counter


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

# Втори начин с метода startswith():

# def count_substring(string, sub_string):
#     count = 0
#     for i in range(len(string)):
#         if string[i:].startswith(sub_string):
#             count += 1
#     return count
#
#
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#
#     count = count_substring(string, sub_string)
#     print(count)
