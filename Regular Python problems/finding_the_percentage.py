students = {}

for current_student in range(int(input())):
    student_data = input().split()

    student_name = student_data[0]
    student_points = list(map(float, student_data[1:]))
    students.update({student_name: student_points})

search_name = input()
result = sum(students[search_name]) / len(students[search_name])
print(f'{result:.2f}')
