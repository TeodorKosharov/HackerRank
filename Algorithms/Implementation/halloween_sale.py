first_game_price, discount, minimum_cost_for_game, budget = [int(x) for x in input().split()]

bought_games = 0
while budget > 0 and budget >= minimum_cost_for_game and budget >= first_game_price:
    if budget >= first_game_price:
        bought_games += 1
        budget -= first_game_price

    first_game_price -= discount
    if first_game_price < minimum_cost_for_game:
        first_game_price = minimum_cost_for_game

print(bought_games)
