# First variant:

# def fibonacci(n):
#     if n == 0:
#         return []
#     elif n == 1:
#         return [0]
#     else:
#         fibonacci_numbers = [0, 1]
#         first_num_index = 0
#         second_num_index = 1
#         for _ in range(n - 2):
#             fibonacci_numbers.append(fibonacci_numbers[first_num_index] + fibonacci_numbers[second_num_index])
#             first_num_index += 1
#             second_num_index += 1
#
#         return fibonacci_numbers
#
#
# cube = lambda x: x ** 3
#
# if __name__ == '__main__':
#     n = int(input())
#     print(list(map(cube, fibonacci(n))))


# Second variant:

def fibonacci(n):
    lis = [0, 1]
    for i in range(2, n):
        lis.append(lis[i - 2] + lis[i - 1])
    return lis[0:n]


cube = lambda x: x ** 3

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
