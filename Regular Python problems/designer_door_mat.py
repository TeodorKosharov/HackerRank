# n, m = list(map(int, input().split()))
#
# special_symbol_repeat = 1
# dash_repeat = (m - 3) // 2
#
# # Top lines:
# for top_line in range(n // 2):
#     print((dash_repeat * '-') + (special_symbol_repeat * '.|.') + (dash_repeat * '-'))
#     special_symbol_repeat += 2
#     dash_repeat -= 3
#
# # Middle line:
# print((((m - 7) // 2) * '-') + 'WELCOME' + (((m - 7) // 2) * '-'))  # m - 7 zashtoto len('WELCOME') = 7
#
# # Bottom lines:
#
# dash_repeat += 3
# special_symbol_repeat -= 2
#
# for bottom_line in range(n // 2):
#     print((dash_repeat * '-') + (special_symbol_repeat * '.|.') + (dash_repeat * '-'))
#     special_symbol_repeat -= 2
#     dash_repeat += 3

N, M = map(int, input().split(" "))

for i in range(N):
    pattern = ".|."
    if i < (N - 1) / 2:
        print((pattern * (2 * i + 1)).center(M, "-"))
    elif i == (N - 1) / 2:
        print("WELCOME".center(M, "-"))
    else:
        print((pattern * (2 * (N - 1 - i) + 1)).center(M, "-"))
