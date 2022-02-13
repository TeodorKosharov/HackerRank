import re

pattern = r'<[a-z]+[\-\.\_0-9a-z]*@[a-z]+\.[a-z]{1,3}>'

for _ in range(int(input())):
    given_email = input()
    if bool(re.match(pattern, given_email.split()[1])):
        print(given_email)
