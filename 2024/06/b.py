#!/usr/bin/python3
import time
from enum import Enum
from dataclasses import dataclass
import argparse
import os

@dataclass
class Point:
    y: int
    x: int 

    def __add__(self, other):
        return Point(self.y + other.y, self.x + other.x)
    
    def __hash__(self):
        return hash((self.y, self.x))


class Direction(Enum):
    UP = Point(-1, 0)
    DOWN = Point(1, 0)
    LEFT = Point(0, -1)
    RIGHT = Point(0, 1)

@dataclass
class Vector:
    y: int
    x: int
    direction: Direction

    def __hash__(self):
        return hash((self.y, self.x, self.direction))

class Guard():
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

def print_grid(grid):
    print( "\n".join(["".join(row) for row in grid]))

def grid_at(grid, loc):
    return grid[loc.y][loc.x] 

def did_loop(guard, grid, new_obstacle):
    visited = set()
    visited.add(Vector(guard.location.y, guard.location.x, guard.dir))

    while True:
        new_location = guard.peek()

        if new_location.y < 0 or new_location.y > len(grid) - 1:
            break
        if new_location.x < 0 or new_location.x > len(grid[0]) -1:
            break

        if grid_at(grid, new_location) != '#' and not (new_location.y == new_obstacle.y and new_location.x == new_obstacle.x):
            guard.move(new_location)

            new_vector = Vector(guard.location.y, guard.location.x, guard.dir)
            if new_vector in visited:
                return True
            visited.add(new_vector)
        else:
            guard.rotate()
    return False
        
            
def run(lines):
    grid = []
    new_grid = []
    guard = None
    original_start = None
    for row_index, row in enumerate(lines):
        grid.append([])
        new_grid.append([])
        for col_index, cell in enumerate(row):
            if cell == '^':
                guard = Guard(row_index, col_index)
                original_start = Point(row_index, col_index)
                grid[row_index].append('^')
                new_grid[row_index].append('#')
                grid[row_index][col_index - 1] = 'O'
            else:
                grid[row_index].append(cell)
                new_grid[row_index].append(cell)
    print_grid(grid)

    original_visited = set()
    original_visited.add(guard.location)
    while True:
        new_location = guard.peek()
        
        if new_location.y < 0 or new_location.y > len(grid) - 1:
            break
        if new_location.x < 0 or new_location.x > len(grid[0]) -1:
            break

        if grid_at(grid, new_location) != '#':
            guard.move(new_location)
            original_visited.add(new_location)
        else:
            guard.rotate()

    # import pdb; pdb.set_trace()
    looped_count = 0
    for new_obstacle in original_visited:
        if did_loop(Guard(original_start.y, original_start.x), grid, new_obstacle):
            print("LOOPED AT ", new_obstacle)
            looped_count += 1

    return looped_count




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