thickness = int(input())
symbol = 'H'

# Top Cone:
print('H'.center(9, ' '))

repeat = 3
for _ in range(4):
    print((repeat * 'H').center(10, ' '))
    repeat += 2

# Top Pillars:
for _ in range(6):
    print(((thickness * 'H').ljust(15, ' ') + (thickness * 'H')).rjust(21, ' '))

# Middle Belt:
for _ in range(3):
    print((24 * 'H').rjust(25, ' '))

# Bottom Pillars:
for _ in range(6):
    print(((thickness * 'H').ljust(15, ' ') + (thickness * 'H')).rjust(21, ' '))

# Bottom Cone:

print((9 * 'H').rjust(22, ' '))

repeat = 7
width = 21
for _ in range(4):
    print((repeat * 'H').rjust(width, ' '))
    repeat -= 2
    width -= 1
