def print_formatted(number):
    x = len(str(bin(n)[2:]))
    for i in range(1, n + 1):
        num = str(i)
        oct_num = str(oct(i)[2:])
        hex_num = str(hex(i)[2:]).upper()
        bin_num = str(bin(i)[2:])
        print(num.rjust(x), oct_num.rjust(x), hex_num.rjust(x), bin_num.rjust(x))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
