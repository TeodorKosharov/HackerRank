from collections import deque

n, k = [int(x) for x in input().split()]
number_of_problems = deque([int(x) for x in input().split()])

page = 0
special_problems = 0

while number_of_problems:
    max_problems_per_page = k
    current_problems = number_of_problems.popleft()
    page += 1

    for problem in range(1, current_problems + 1):
        if problem == page:
            special_problems += 1

        if problem == max_problems_per_page and problem != current_problems:
            page += 1
            max_problems_per_page += k

print(special_problems)
