import re

pattern = r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])[AEIOUaeiou]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])'
inp = input()

matches = re.findall(pattern, inp)

if matches:
    for match in matches:
        print(match)
else:
    print(-1)
