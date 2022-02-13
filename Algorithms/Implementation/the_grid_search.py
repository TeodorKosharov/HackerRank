def match_check(m_grid: list, p_grid: list, p_rows, p_cols, c_row, c_col):
    # p_rows -> pattern_rows
    # p_cols -> pattern_cols
    # c_row -> check_row
    # c_col -> check_col

    pat_grid_row = 0
    pat_grid_col = 0

    for r in range(p_rows):
        for c in range(p_cols):
            if m_grid[c_row + r][c_col + c] != p_grid[pat_grid_row][pat_grid_col]:
                return False
            pat_grid_col += 1
            if pat_grid_col == pattern_cols:
                pat_grid_col = 0

        if pat_grid_row == pattern_rows:
            pat_grid_row = 0
            continue

        pat_grid_row += 1

    return True


for case in range(int(input())):
    main_grid = []
    pattern_grid = []
    grid_rows, grid_cols = map(int, input().split())

    for row in range(grid_rows):
        main_grid.append(tuple(input()))

    pattern_rows, pattern_cols = map(int, input().split())

    for row in range(pattern_rows):
        pattern_grid.append(tuple(input()))

    end_row = grid_rows - pattern_rows + 1
    end_col = grid_cols - pattern_cols + 1
    is_match_found = False

    for check_row in range(end_row):
        for check_col in range(end_col):
            if match_check(main_grid, pattern_grid, pattern_rows, pattern_cols, check_row, check_col):
                print('YES')
                is_match_found = True
                break
        if is_match_found:
            break

    if not is_match_found:
        print('NO')
