import re

pattern = r'[7|8|9]{1}[0-9]{9}\b'

for _ in range(int(input())):
    if bool(re.match(pattern, input())):
        print('YES')
    else:
        print('NO')
