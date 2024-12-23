#!/usr/bin/python3
import time
import copy
from collections import defaultdict, deque
from dataclasses import dataclass
import argparse
import sys
import os

@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

UP = Point(-1, 0)
DOWN = Point(1, 0)
LEFT = Point(0, -1)
RIGHT = Point(0, 1)
directions = [UP, DOWN, LEFT, RIGHT]

class Grid:
    def __init__(self):
        self.grid = defaultdict(lambda: '.')
        self.max_x = -1
        self.max_y = -1
        self.start_point = None
        self.end_point = None

    def make_key(self, point):
        return f"{point.x}:{point.y}"

    def v(self, x, y):
        return self.v_at_point(Point(x, y))
        
    def v_at_point(self, point):
        k = self.make_key(point)

        if point.x < 0 or point.y < 0:
            return None
        
        if point.x > self.max_x or point.y > self.max_y :
            return None

        return self.grid[k]

    def add_point(self, point, value):
        k = self.make_key(point)
        self.grid[k] = value
        if value == 'S':
            self.start_point = point
        elif value == 'E':
            self.end_point = point
        self.max_x = max(point.x, self.max_x)
        self.max_y = max(point.y, self.max_y)

    def print(self):
        for y in range(0, self.max_y + 1):
            line = []
            for x in range(0, self.max_x + 1):
                line.append(self.v(x, y))
            print("".join(line))
        print()

def find_shortest_path(grid):
    depths = {}
    # make a queue
    q = deque([(grid.start_point, 0)])
    seen = set()
    
    while len(q):
        current, depth = q.popleft()

        if current in seen:
            continue

        depths[current] = depth

        # if depth > 81:
        #     import pdb; pdb.set_trace()
        if current == grid.end_point:
            return depths

        
        seen.add(current)

        for direction in directions:
            new_point = current + direction

            grid_value = grid.v_at_point(new_point)
            if not grid_value:
                continue
                
            if grid_value == '#':
                continue

            q.append((new_point, depth + 1))


def run(lines):
    grid = Grid()

    for y, line in enumerate(lines):
        for x, cell in enumerate(line):
            grid.add_point(Point(int(x), int(y)), cell)
    
    grid.print()

    count = 0
    depths = find_shortest_path(grid)

    # debug
    # list_of_depths = defaultdict(list)
    # # print depths
    # for point, depth in depths.items():
    #     list_of_depths[depth].append(point)
    
    # for depth, points in list_of_depths.items():
    #     grid_copy = copy.deepcopy(grid)
    #     for point in points:
    #         k = grid.make_key(point)
    #         grid_copy.grid[k] = 'O'
    #     print(depth)
    #     grid_copy.print()
    #     time.sleep(0.1)        
        
    counts = defaultdict(int)
    for y in range(0, grid.max_y + 1):
        for x in range(0, grid.max_x + 1):
            value = grid.v(x, y)
            if value == '#':
                current_wall = Point(x, y)
                for (dir1, dir2) in ((UP, DOWN), (LEFT, RIGHT)):

                # look in orthogonal directions
                    p1 = current_wall + dir1
                    p2 = current_wall + dir2

                    v1 = grid.v_at_point(p1)
                    v2 = grid.v_at_point(p2)

                    if not v1 or not v2:
                        continue

                    if v1 == '#' or v2 == '#':
                        continue

                    delta = abs(depths[p2] - depths[p1])
                    if delta > 100:
                        count += 1
                    # start = p1
                    # end = p2
                    counts[delta - 2] += 1
                        # print(delta)
                # start = Point(x, y)
                # for direction in directions:
                #     end = start + direction

                #     grid_value = grid.v_at_point(end)
                #     if not grid_value:
                #         continue

                #     if grid_value != '.':
                #         continue

                #     import pdb; pdb.set_trace()
    print(counts)
    return count
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='run.py')
    parser.add_argument('-x', '--example', action='store_true')
    args = parser.parse_args()

    filename = 'input-example.txt' if args.example else 'input.txt'

    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, filename), 'r') as f:
        answer = run(f.read().splitlines())
        print("### ANSWER ### ")
        print(answer)