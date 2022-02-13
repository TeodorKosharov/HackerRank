students = []
scores = []
names = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

    scores.append(score)
    scores = list(set(scores))
    scores.sort(reverse=True)
    if _ > 2:
        second_lowest_score = scores[-2]
    elif _ <= 1:
        second_lowest_score = scores[0]

for mini_list in students:
    if second_lowest_score == mini_list[1]:
        names.append(mini_list[0])

names.sort()
for i in names:
    print(i)
