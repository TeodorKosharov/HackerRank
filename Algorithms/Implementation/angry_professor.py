for test_case in range(int(input())):
    students, cancellation_treshold = map(int, input().split())
    students_arrival_times = map(int, input().split())

    late_students = len([x for x in students_arrival_times if x < 1])

    if late_students >= cancellation_treshold:
        print('NO')
    elif late_students < cancellation_treshold:
        print('YES')
