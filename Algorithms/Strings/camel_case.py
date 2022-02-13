given_string = input()
counter = 1 + len([char for char in given_string if char.isupper()])
print(counter)
