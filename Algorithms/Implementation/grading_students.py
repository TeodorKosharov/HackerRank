def get_multiple_of_five(value: int):
    for x in range(10):
        value += 1
        if value % 5 == 0:
            return value


for i in range(int(input())):
    grade = int(input())
    if grade >= 38:
        rounded_grade = get_multiple_of_five(grade)
        if abs(rounded_grade) - grade < 3:
            print(rounded_grade)
        else:
            print(grade)

    else:
        print(grade)
