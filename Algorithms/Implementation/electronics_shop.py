budget, keyboards, drives = list(map(int, input().split()))
keyboards_prices = list(map(int, input().split()))
drives_prices = list(map(int, input().split()))

max_combination = 0

for keyboard_price in keyboards_prices:
    for driver_price in drives_prices:
        if (keyboard_price + driver_price) <= budget and (keyboard_price + driver_price) > max_combination:
            max_combination = keyboard_price + driver_price

print(-1 if max_combination == 0 else max_combination)
