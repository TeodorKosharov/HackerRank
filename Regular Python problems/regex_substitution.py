import re

for line in range(int(input())):
    sample = input()
    while ' && ' in sample:
        sample = re.sub(' && ', ' and ', sample)
    while ' || ' in sample:
        sample = re.sub(r' \|\| ', ' or ', sample)
    print(sample)
