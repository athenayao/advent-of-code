
# - If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# - If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# - Otherwise, the seat's state does not change.

EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'

def occupied(value):
    return value == OCCUPIED
    
def count_adjacent_occupied(grid, y, x):
    row_length = len(grid[0])
    count = 0
    if y > 0: 
        if x > 0 and occupied(grid[y - 1][x - 1]):
            count += 1
        if occupied(grid[y - 1][x]):
            count += 1
        if x + 1 < row_length and occupied(grid[y - 1][x + 1]):
            count += 1

    if x > 0 and occupied(grid[y][x - 1]):
        count += 1
    if x + 1 < row_length and occupied(grid[y][x + 1]):
        count += 1

    if y + 1 < len(grid):
        if occupied(grid[y + 1][x]):
            count += 1
        if x > 0 and occupied(grid[y + 1][x - 1]):
            count += 1
        if x + 1 < row_length  and occupied(grid[y + 1][x + 1]):
            count += 1

    return count

def update_grid(grid):
    new_grid = []

    for row_index, row in enumerate(grid):
        new_grid.append([])
        for cell_index, cell_value in enumerate(row):
            if cell_value == FLOOR:
                new_grid[row_index].append(FLOOR)
            elif cell_value == EMPTY:
                if count_adjacent_occupied(grid, row_index, cell_index) == 0:
                    new_grid[row_index].append(OCCUPIED)
                else:
                    new_grid[row_index].append(EMPTY)
            elif cell_value == OCCUPIED:
                if count_adjacent_occupied(grid, row_index, cell_index) >= 4:
                    new_grid[row_index].append(EMPTY)
                else:
                    new_grid[row_index].append(OCCUPIED)
    return new_grid

def count_occupied(grid):
    count = 0
    for row in grid:
        for cell in row:
            if cell == OCCUPIED:
                count += 1
    return count

def print_grid(grid):
    print("-- GRID --")
    for row in grid:
        print("".join(row))
    

def run(grid):
    previous_grid = None
    while grid != previous_grid:
        previous_grid = grid
        grid = update_grid(grid)
    return count_occupied(grid)


if __name__ == '__main__':
    is_example = False
    with open('./input-example.txt' if is_example else './input.txt', 'r') as f:
        answer = run(f.read().splitlines())
        print("### ANSWER ### ")
        print(answer)
