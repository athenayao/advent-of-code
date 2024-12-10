#!/usr/bin/python3
from dataclasses import dataclass
import argparse
import sys
import os

@dataclass(frozen=True)
class Point:
    y: int
    x: int
def make_grid(lines):
    grid = []

    for line in lines:
        row = []
        grid.append(row)
        for char in line:
            if char == '.':
                row.append('.')
            else:
                row.append(int(char))
    return grid

UP = Point(-1, 0)
DOWN = Point(1, 0)
LEFT = Point(0, -1)
RIGHT = Point(0, 1)

directions = [UP, DOWN, LEFT, RIGHT]

def find_trail(grid, y, x, level):
    start_at = Point(y, x)

    if level == 10:
        return 1

    num_trails = 0
    for d in directions:
        new_point = Point(start_at.y + d.y, start_at.x + d.x)
        if new_point.y < 0 or new_point.x < 0:
            continue
        if new_point.y > len(grid)-1 or new_point.x > len(grid[0]) -1:
            continue
        if grid[new_point.y][new_point.x] == level:
            num_trails += find_trail(grid, new_point.y, new_point.x, level + 1)

    return num_trails
    

def find_score(grid, y, x):
    trail = find_trail(grid, y, x, 1)
    return trail


def run(lines):
    grid = make_grid(lines)

    score = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 0:
                cur_score = find_score(grid, y, x)
                score += cur_score
    return score
                
                

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