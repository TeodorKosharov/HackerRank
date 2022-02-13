# First variant with strings:

# for i in range(1, int(input())):
#     print(i * f'{i}')


# Second variant with formula:

for i in range(1, int(input())):
    print((10 ** i // 9) * i)
