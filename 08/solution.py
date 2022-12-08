#! python3
import sys

def scan_direction(x, y, grid, direction):
    # probably more efficient to just scan once
    current = grid[y][x]

    # import pdb; pdb.set_trace()
    if direction == 'left':
        range_x = range(x - 1, 0 - 1, -1)
    elif direction == 'right':
        range_x = range(x + 1, len(grid), 1)
    if direction == 'left' or direction == 'right':
        for delta_x in range_x:
            # print(current, grid[y][delta_x], direction)
            if current <= grid[y][delta_x]:
                return False
        return True

    if direction == 'up':
        range_y = range(y - 1, 0 - 1, -1)
    elif direction == 'down':
        range_y = range(y + 1, len(grid), 1)
    if direction == 'up' or direction == 'down':
        for delta_y in range_y:
            # print(current, grid[delta_y][x], direction)
            if current <= grid[delta_y][x]:
                return False
        return True


def run_part_1(filename):
    grid = []
    with open(filename, 'r') as file:
        for raw_line in file.readlines():
            line = raw_line.strip()
            grid.append(list(line))

        num_visible = 0
        size = len(grid)
        for row_index, row in enumerate(grid):
            for col_index, char in enumerate(row):
                is_edge = row_index == 0 or row_index == size - 1 or col_index == 0 or col_index == size - 1
                if is_edge:
                    num_visible += 1
                    continue
                # print("scanning ", row_index, col_index)
                if scan_direction(col_index, row_index, grid, 'left') \
                    or scan_direction(col_index, row_index, grid, 'right') \
                    or scan_direction(col_index, row_index, grid, 'up') \
                    or scan_direction(col_index, row_index, grid, 'down'):
                    # print(grid[col_index][row_index], row_index, col_index, left, right, up, down)
                    num_visible += 1
                    
        print(num_visible)



def count_direction(x, y, grid, direction):
    # probably more efficient to just scan once
    current = grid[y][x]

    count = 0
    if direction == 'left':
        range_x = range(x - 1, 0 - 1, -1)
    elif direction == 'right':
        range_x = range(x + 1, len(grid), 1)
    if direction == 'left' or direction == 'right':
        for delta_x in range_x:
            count += 1
            if current <= grid[y][delta_x]:
                break
        return count

    if direction == 'up':
        range_y = range(y - 1, 0 - 1, -1)
    elif direction == 'down':
        range_y = range(y + 1, len(grid), 1)
    if direction == 'up' or direction == 'down':
        for delta_y in range_y:
            # print(current, grid[delta_y][x], direction)
            count += 1
            if current <= grid[delta_y][x]:
                break
        return count

def run_part_2(filename):
    grid = []
    with open(filename, 'r') as file:
        for raw_line in file.readlines():
            line = raw_line.strip()
            grid.append(list(line))

        num_visible = 0
        size = len(grid)
        current_max = 0
        for row_index, row in enumerate(grid):
            for col_index, char in enumerate(row):
                is_edge = row_index == 0 or row_index == size - 1 or col_index == 0 or col_index == size - 1
                if is_edge:
                    num_visible += 1
                    continue

                # memoize grid scan directions?
                left = count_direction(col_index, row_index, grid, 'left')
                right = count_direction(col_index, row_index, grid, 'right')
                up = count_direction(col_index, row_index, grid, 'up')
                down = count_direction(col_index, row_index, grid, 'down')
                scenic_score = left * right * up * down
                current_max = max(current_max, scenic_score)
                # print(char, row_index, col_index, '[', left, right, up, down, ']')
                    
        print(current_max)



if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else None
    if not mode:
        mode == "ax"

    if mode == "ax":
        run_part_1('./sample-input.txt')
    elif mode == "a":
        run_part_1("./input.txt")
    elif mode == "bx":
        run_part_2('./sample-input.txt')
    elif mode == "b":
        run_part_2('./input.txt')