year = int(input())

if year == 1918:
    print('26.09.1918')
elif year < 1917:
    if year % 4 == 0:
        print(f"12.09.{year}")
    else:
        print(f'13.09.{year}')
elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'12.09.{year}')
else:
    print(f'13.09.{year}')
