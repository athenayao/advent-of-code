#!/usr/bin/python3
from collections import namedtuple, defaultdict
import argparse
import sys
import os

Point = namedtuple('Point', 'x, y')
class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


RIGHT = Point(1, 0)
LEFT = Point(-1, 0)
UP = Point(0, -1)
DOWN = Point(0, 1)

 # lazy
energized = set()
points = []

def print_grid(grid):
    print('\n'.join([''.join(['#' if Point(x, y) in energized else '.' for x, _ in  enumerate(l)]) for y, l in enumerate(grid)]))

def move(grid, start, direction, visited):
    if (start, direction) in visited or start.y < 0 or start.y >= len(grid) or start.x < 0 or start.x >= len(grid[0]):
        return
    current_point = grid[start.y][start.x]
    visited.add((start, direction))
    energized.add(start)

    new_direction = None

    if current_point == '.':
        new_direction = direction
    elif current_point == '\\':
        if direction == RIGHT:
            new_direction = DOWN
        elif direction == LEFT:
            new_direction = UP
        elif direction == UP:
            new_direction = LEFT
        elif direction == DOWN:
            new_direction = RIGHT
    elif current_point == '/':
        if direction == RIGHT:
            new_direction = UP
        elif direction == LEFT:
            new_direction = DOWN
        elif direction == UP:
            new_direction = RIGHT
        elif direction == DOWN:
            new_direction = LEFT
    elif current_point == '|':
        if direction == UP or direction == DOWN:
            new_direction = direction
        else:
            points.append((start + UP, UP))
            points.append((start + DOWN, DOWN))
            return
    elif current_point == '-':
        if direction == LEFT or direction == RIGHT:
            new_direction = direction
        else:
            points.append((start + LEFT, LEFT))
            points.append((start + RIGHT, RIGHT))
            return

    return move(grid, start + new_direction, new_direction, visited)


def run(lines):
    grid = []
    for y, line in enumerate(lines):
        grid.append([])
        for x, cell in enumerate(line):
            grid[y].append(cell)
    
    points.append((Point(0, 0), RIGHT))
    visited = set()
    # depth first search
    while points:
        (current_point, direction) = points.pop()
        move(grid, current_point, direction, visited)

    return len(energized)


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