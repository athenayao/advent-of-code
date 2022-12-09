
# - If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# - If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# - Otherwise, the seat's state does not change.

EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'

class XDelta(object):
    LEFT = -1
    CENTER = 0
    RIGHT = 1

class YDelta(object):
    UP = -1
    CENTER = 0
    DOWN = 1


def occupied(value):
    return value == OCCUPIED

def peek_nearest_seat(grid, y, x, y_delta, x_delta):
    new_y = y
    new_x = x

    while True:
        new_y = new_y + y_delta
        new_x = new_x + x_delta

        if new_y < 0 or new_y > len(grid) - 1:
            return 0

        if new_x < 0 or new_x > len(grid[0]) - 1:
            return 0
        
        if grid[new_y][new_x] == EMPTY:
            return 0

        if grid[new_y][new_x] == OCCUPIED:
            return 1

def count_nearest_occupied(grid, y, x):
    row_length = len(grid[0])
    count = 0

    # . . .
    count += peek_nearest_seat(grid, y, x, YDelta.UP, XDelta.LEFT)
    count += peek_nearest_seat(grid, y, x, YDelta.UP, XDelta.CENTER)
    count += peek_nearest_seat(grid, y, x, YDelta.UP, XDelta.RIGHT)

    # . x .
    count += peek_nearest_seat(grid, y, x, YDelta.CENTER, XDelta.LEFT)
    count += peek_nearest_seat(grid, y, x, YDelta.CENTER, XDelta.RIGHT)

    # . . .
    count += peek_nearest_seat(grid, y, x, YDelta.DOWN, XDelta.LEFT)
    count += peek_nearest_seat(grid, y, x, YDelta.DOWN, XDelta.CENTER)
    count += peek_nearest_seat(grid, y, x, YDelta.DOWN, XDelta.RIGHT)

    # print("count (%s, %s) = %s" % (y, x, count))
    return count

def update_grid(grid):
    new_grid = []

    for row_index, row in enumerate(grid):
        new_grid.append([])
        for cell_index, cell_value in enumerate(row):
            if cell_value == FLOOR:
                new_grid[row_index].append(FLOOR)
            elif cell_value == EMPTY:
                if count_nearest_occupied(grid, row_index, cell_index) == 0:
                    new_grid[row_index].append(OCCUPIED)
                else:
                    new_grid[row_index].append(EMPTY)
            elif cell_value == OCCUPIED:
                if count_nearest_occupied(grid, row_index, cell_index) >= 5:
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
