message = input()

start = 0
changed_letters = 0
for i in range(3, len(message) + 3, 3):
    substring = message[start: i]
    if substring[0] != 'S':
        changed_letters += 1
    if substring[1] != 'O':
        changed_letters += 1
    if substring[2] != 'S':
        changed_letters += 1
    start += 3

print(changed_letters)
