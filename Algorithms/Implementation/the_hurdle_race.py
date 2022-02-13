n, possible_jump = map(int, input().split())
heights = list(map(int, input().split()))

needed_potions = 0

for current_height in heights:
    if current_height > possible_jump:
        needed_potions += current_height - possible_jump
        possible_jump += current_height - possible_jump

print(needed_potions)
