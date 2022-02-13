n = int(input())
password = input()

added_chars = 0
special_additions = 0

if not [char for char in password if char.isdigit()]:
    added_chars += 1

if not [char for char in password if char.isupper()]:
    added_chars += 1

if not [char for char in password if char.islower()]:
    added_chars += 1

if not [char for char in password if char in '!@#$%^&*()-+']:
    added_chars += 1

if len(password) < 6:
    if len(password) + added_chars < 6:
        added_chars += 6 - len(password) - added_chars

print(added_chars)
