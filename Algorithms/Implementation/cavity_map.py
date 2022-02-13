size = int(input())

square_map = []

for row in range(size):
    current_row = list(input())
    square_map.append([int(x) for x in current_row])

cavity_coords = []

for row in range(1, size - 1):
    for col in range(1, size - 1):
        current_value = square_map[row][col]
        upper_value = square_map[row - 1][col]
        down_value = square_map[row + 1][col]
        left_value = square_map[row][col - 1]
        right_value = square_map[row][col + 1]

        cavity_conditions = [
            current_value > upper_value,
            current_value > down_value,
            current_value > left_value,
            current_value > right_value
        ]

        if all(cavity_conditions):
            cavity_coords.append((row, col))

for cavity in cavity_coords:
    square_map[cavity[0]][cavity[1]] = 'X'

for row in square_map:
    print(*row, sep='')
