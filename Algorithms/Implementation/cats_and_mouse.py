for case in range(int(input())):
    first_cat_position, second_cat_position, mouse_position = map(int, input().split())
    first_cat_distace_to_mouse = abs(first_cat_position - mouse_position)
    second_cat_distance_to_mouse = abs(second_cat_position - mouse_position)

    if first_cat_distace_to_mouse < second_cat_distance_to_mouse:
        print('Cat A')
    elif first_cat_distace_to_mouse > second_cat_distance_to_mouse:
        print('Cat B')
    else:
        print('Mouse C')
