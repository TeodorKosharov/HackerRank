first_start, first_step, second_start, second_step = list(map(int, input().split()))

if (first_step > second_step) and (second_start - first_start) % (second_step - first_step) == 0:
    print('YES')
else:
    print('NO')
