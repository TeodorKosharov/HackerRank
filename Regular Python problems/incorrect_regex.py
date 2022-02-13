import re

for i in range(int(input())):
    valid = True
    try:
        regex = re.compile(input())
    except re.error:
        valid = False
    print(valid)
