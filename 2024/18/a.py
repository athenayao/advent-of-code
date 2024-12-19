#!/usr/bin/python3
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

directions = [Point(-1, 0), Point(1, 0), Point(0, -1), Point(0, 1)]

class Grid:
    def __init__(self):
        self.grid = defaultdict(lambda: '.')
        self.max_x = -1
        self.max_y = -1

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

    def add_point(self, point):
        k = self.make_key(point)
        self.grid[k] = "#"
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
    # make a queue
    q = deque([(Point(0, 0), 0)])
    seen = set()
    
    while len(q):
        current, depth = q.popleft()

        if current == Point(grid.max_x, grid.max_y):
            return depth

        if current in seen:
            continue

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


    for line in lines:
        x, y = line.split(',')
        grid.add_point(Point(int(x), int(y)))
    
    grid.print()

    return find_shortest_path(grid)
    
    


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