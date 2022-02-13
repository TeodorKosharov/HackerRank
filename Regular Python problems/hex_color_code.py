import re

pattern = r'#[0-9a-fA-F]{3}\b|#[0-9a-fA-F]{6}\b'
is_selector = True

for _ in range(int(input())):
    line = input()
    if '{' in line:
        is_selector = False
        continue
    elif '}' in line:
        is_selector = True

    if not is_selector:
        mathes = re.findall(pattern, line)
        for match in mathes:
            print(match)
