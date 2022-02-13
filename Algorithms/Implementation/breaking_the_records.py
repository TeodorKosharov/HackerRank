n = int(input())
scores = list(map(int, input().split()))

max_score = scores[0]
min_score = scores[0]

maxes = 0
mins = 0

for score in scores:
    if score > max_score:
        max_score = score
        maxes += 1
    elif score < min_score:
        min_score = score
        mins += 1

print(maxes, mins)
