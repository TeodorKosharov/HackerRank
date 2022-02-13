for case in range(int(input())):
    budget, choco_bar_cost, needed_wrappers = [int(x) for x in input().split()]

    bought_bars = budget // choco_bar_cost
    produced_wrappers = bought_bars

    while produced_wrappers >= needed_wrappers:
        additional_bars = produced_wrappers // needed_wrappers
        bought_bars += additional_bars
        produced_wrappers = additional_bars + produced_wrappers % needed_wrappers

    print(bought_bars)
