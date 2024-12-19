#!/usr/bin/python3
import time
import copy
from enum import Enum
from dataclasses import dataclass
import argparse
import os

@dataclass(frozen=True)
class Point:
    y: int
    x: int

    def __add__(self, other):
        return Point(self.y + other.y, self.x + other.x)

class Direction(Enum):
    UP = Point(-1, 0)
    DOWN = Point(1, 0)
    LEFT = Point(0, -1)
    RIGHT = Point(0, 1)



def print_grid(grid):
    print("\n".join(["".join(row) for row in grid]))

class Reindeer():
    def __init__(self, y, x):
        self.location = Point(y, x)
        self.dir = '^'
        self.dir_index = 0
        self.directions = ['^', '>', 'v', '<']
    
    def peek(self):
        if self.dir == '^':
            return self.location + Direction.UP.value
        if self.dir == '>':
            return self.location + Direction.RIGHT.value
        if self.dir == 'v':
            return self.location + Direction.DOWN.value
        if self.dir == '<':
            return self.location + Direction.LEFT.value

    def rotate(self):
        self.dir_index = (self.dir_index + 1) % len(self.directions) 
        self.dir = self.directions[self.dir_index]

    def move(self, new_location):
        self.location = new_location

def find_path(grid, end_point, current_point, seen, grid_copy):
    print(current_point)
    print_grid(grid_copy)
    # already seen, don't go down this path

    seen.add(current_point)
    if current_point == end_point:
        return 1

    totals = []
    for delta in [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]:
        new_point = current_point + delta.value

        new_value = grid_at(grid, new_point)
        if new_value == '#':
            continue

        grid_copy[new_point.y][new_point.x] = '?'

        if new_point in seen:
            continue

        results = 1 + find_path(grid, end_point, new_point, seen, grid_copy)
        totals.append(results)
    if totals:
        return min(totals)
    return float('inf')


def grid_at(grid, loc):
    return grid[loc.y][loc.x] 

def run(lines):
    grid = []

    start_point = None
    end_point = None
    for y, line in enumerate(lines):
        grid.append([])
        for x, cell in enumerate(line):
            grid[y].append(cell)
            if cell == 'S':
                start_point = Point(y, x)
            elif cell == 'E':
                end_point = Point(y, x)

    grid_copy = copy.deepcopy(grid)
    results = find_path(grid, end_point, start_point, set(), grid_copy)
    return results

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