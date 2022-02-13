for testcase in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except ZeroDivisionError as err:
        print(f'Error Code: {err}')
    except ValueError as err:
        print(f'Error Code: {err}')
