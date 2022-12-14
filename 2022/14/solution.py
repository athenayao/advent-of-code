#! python3
import sys
from enum import Enum

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.x}:{self.y}'


class Objects(Enum):
    AIR = 0
    ROCK = 1
    SAND = 2
    FALLING_SAND = 3

    def __repr__(self):
        if  self.name == 'ROCK':
            return '#'
        elif self.name == 'SAND':
            return 'o'
        elif self.name == 'FALLING_SAND':
            return '+'
        
    def __str__(self):
        return self.__repr__()

class Cave:
    def __init__(self):
        self.grid = {}
        self.max_rocks = 0
        self.min_x = float('inf')
        self.max_x = float('-inf')
    
    def add_rocks(self, all_lines):
        for raw_line in all_lines:
            line = raw_line.strip()
            paths = line.split( "-> ")

            point = None
            prev_point = None
            for path in paths:
                prev_point = point

                # x: distance to the right
                # y: distance down
                (x, y) = [int(item) for item in path.split(",")]
                self.min_x = min(x, self.min_x)
                self.max_x = max(x, self.max_x)
                point = Point(x, y)
                self.add(point, Objects.ROCK)
                if prev_point is not None:
                    for x in range(min(point.x, prev_point.x) + 1, max(point.x, prev_point.x)):
                        new_point = Point(x, point.y)
                        self.add(new_point, Objects.ROCK)
                    
                    for y in range(min(point.y, prev_point.y) + 1, max(point.y, prev_point.y)):
                        new_point = Point(point.x, y)
                        self.add(new_point, Objects.ROCK)

    def add(self, point, value, ignore_max=False):
        self.grid[str(point)] = value
        if not ignore_max:
            self.max_rocks = max(self.max_rocks, point.y)

    def get(self, point):
        key = str(point)
        if key in self.grid:
            return self.grid[key]
        return '.'
    
    def occupied(self, point):
        key = str(point)
        return key in self.grid

    def print(self):
        print(self.grid)
        for row_index, y in enumerate(range(0, 12)):
            row = [str(row_index), '']
            for x in range(490, 510):
                point = Point(x, y)
                row.append(str(self.get(point)))
            print(''.join(row))

        
    def descend(self, sand):
        for direction in [
            Point(sand.x, sand.y + 1), # down
            Point(sand.x - 1, sand.y + 1), # down-left
            Point(sand.x + 1, sand.y + 1), # down-right
        ]:
            if not self.occupied(direction):
                return direction
        return None

    def drop_sand(self):
        sand = Point(500,0)
        while True:
            new_position = self.descend(sand)
            if new_position is None:
                self.add(sand, Objects.SAND)
                return False
            else: 
                sand = new_position
            if sand.y > self.max_rocks:
                return True
    
    def drop_sand_until_full(self):
        sand = Point(500,0)
        while True:
            new_position = self.descend(sand)
            if new_position is None:
                if sand.x == 500 and sand.y == 0:
                    return True
                self.add(sand, Objects.SAND)
                return False
            else: 
                sand = new_position

    
def run_part_1(filename):
    cave = Cave()

    with open(filename, 'r') as file:
        cave = Cave()
        cave.add_rocks(file.readlines())
    
        counter = 0
        while True:
            is_full = cave.drop_sand()
            if is_full:
                break
            else:
                counter += 1
        print(counter)


def run_part_2(filename):
    with open(filename, 'r') as file:
        cave = Cave()
        cave.add_rocks(file.readlines())

        for x in range(cave.min_x - 200, cave.max_x + 200):
            point = Point(x, cave.max_rocks + 2)
            cave.add(point, Objects.ROCK, ignore_max=True)
        cave.max_rocks += 2


        counter = 0
        while True:
            counter += 1
            is_full = cave.drop_sand_until_full()
            if is_full:
                break
        print(counter)

        


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