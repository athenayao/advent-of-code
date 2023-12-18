#!/usr/bin/python3
import argparse
import sys
import os
import re

LINE_REGEX = re.compile('(?P<direction>[RLDU]) (?P<times>\d+)')

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __hash__(self):
        return hash((self.x, self.y))


directions = {
    'R': Point(1, 0),
    'L': Point(-1, 0),
    'U': Point(0, -1),
    'D': Point(0, 1),
}

UNKNOWN = '-'

# maybe this make_grid doesn't matter
def make_grid(seen_points):
    min_x = float("inf")
    min_y = float("inf")
    max_y = float("-inf")
    max_x = float("-inf")

    for point in seen_points:
        min_x = min(point.x, min_x)
        min_y = min(point.y, min_y)
        max_x = max(point.x, max_x)
        max_y = max(point.y, max_y)
    
    grid = []
    for y in range(min_y, max_y + 1):
        line = []
        grid.append(line)
        for x in range(min_x, max_x + 1):
            p = Point(x, y)
            if p == Point(0, 0):
                line.append('!')
            elif p in seen_points:
                line.append('#')
            else:
                line.append(UNKNOWN)
    
    return grid

def print_grid(grid):
    print('\n'.join((''.join(line) for line in grid)))

# make a bfs

def flood(border, start):
    visited = set()
    points_to_process = [start]
    dug = set(border)

    # import pdb; pdb.set_trace()
    while points_to_process:
        point = points_to_process.pop()
        visited.add(point)

        for x in range(point.x - 1, point.x + 2):
            for y in range(point.y - 1, point.y + 2):
                adj_point = Point(x, y)
                if adj_point in visited:
                    continue
                if adj_point in border:
                    continue
                
                points_to_process.append(adj_point)
    return len(border) + len(visited)


def run(lines):
    seen_points = set()
    x = 0
    y = 0

    point = Point(0, 0)
    seen_points.add(point)

    dirs = []
    for line in lines:
        match = LINE_REGEX.match(line)
        direction = match.group('direction')
        times = int(match.group('times'))
        dirs.append(direction)

        for _ in range(0, times):
            point += directions[direction]
            seen_points.add(point)

    first_interior_point = Point(0, 0) + directions[dirs[0]] + directions[dirs[1]]
    
    grid = make_grid(seen_points)
    print_grid(grid)
    return flood(seen_points, first_interior_point)
    

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