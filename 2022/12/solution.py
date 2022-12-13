#! python3
import sys
from enum import Enum
from collections import namedtuple

Point = namedtuple('Point', 'row, col')

class Grid:
    def __init__(self, grid):
        self.grid = grid
    
    def get_value(self, point):
        return ord(self.grid[point.row][point.col])

    def get_char(self, point):
        return self.grid[point.row][point.col]
    
    def get_destination(self, origin, direction):
        point = Point(origin.row + direction.row, origin.col + direction.col)
        if point.row < 0 or point.row >= len(self.grid) or point.col < 0 or point.col >= len(self.grid[0]):
            return None
        return point

    def num_cells(self):
        return len(self.grid) * len(self.grid[0])



class Directions(Enum):
    UP = Point(-1, 0)
    DOWN = Point(1, 0)
    LEFT = Point(0, -1)
    RIGHT = Point(0, 1)


#TODO 1: make this BFS
def find_path(grid, start, end, seen, path = None):
    origin_value = grid.get_value(start)

    seen = set(seen)
    seen.add(start)
    path = list(path)
    path.append(start)
    # print("path", path)

    if start == end:
        # print("path", path)
        return len(seen) - 1

    min_len = grid.num_cells()
    for direction in Directions:
        destination = grid.get_destination(start, direction.value)
        if destination is None:
            continue

        if destination in seen:
            continue

        if origin_value - grid.get_value(destination) <= 1:
            min_len = min(find_path(grid, destination, end, seen, path), min_len)
    return min_len


def run_part_1(filename):
    with open(filename, 'r') as file:
        grid = []
        start = None
        end = None

        for row_index, raw_line in enumerate(file.readlines()):
            line = raw_line.strip()

            row = []
            for col_index, char in enumerate(list(line)):
                if char == 'S':
                    char = 'a'
                    start = Point(row_index, col_index)
                elif char == 'E':
                    char = 'z'
                    end = Point(row_index, col_index)
                row.append(char)
            grid.append(row)

        print(find_path(Grid(grid), end, start, set(), []))


def run_part_2(filename):
    with open(filename, 'r') as file:
        for raw_line in file.readlines():
            line = raw_line.strip()
            print(".." + line)
            # do something


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else None
    if not mode:
        mode == "ax"

    if mode == "ax":
        run_part_1('./example.txt')
    elif mode == "a":
        run_part_1("./input.txt")
    elif mode == "bx":
        run_part_2('./example.txt')
    elif mode == "b":
        run_part_2('./input.txt')