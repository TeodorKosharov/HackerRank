scores = {'Alice': 0, 'Bob': 0}

a_integers = [int(x) for x in input().split()]
b_integers = [int(x) for x in input().split()]

for i in range(len(a_integers)):
    if a_integers[i] > b_integers[i]:
        scores['Alice'] += 1
    elif a_integers[i] < b_integers[i]:
        scores['Bob'] += 1

print(' '.join(map(str, scores.values())))
