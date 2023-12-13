#!/usr/bin/python3
from collections import namedtuple, defaultdict
import argparse
import sys
import os

Point = namedtuple('Point', 'x, y')

def find_manhattan_distance(point1, point2):
    return abs(point1.x - point2.x) + abs(point1.y - point2.y)


def run(lines):
    galaxy_rows = defaultdict(bool)
    galaxy_cols = defaultdict(bool)
    galaxies = []

    for y, row in enumerate(lines):
        for x, char in enumerate(list(row)):
            galaxy_rows[y] = galaxy_rows[y] or False
            galaxy_cols[x] = galaxy_cols[x] or False
            if char == '#':
                galaxy_rows[y] = galaxy_rows[y] or True
                galaxy_cols[x] = galaxy_cols[x] or True

    
    expand_factor = 1000000 - 1
    expanded_universe = []
    for y, row in enumerate(lines):
        new_row = []
        for x, char in enumerate(list(row)):
            if not galaxy_cols[x]:
                for _ in range(0,  expand_factor):
                    new_row.append('.')

            new_row.append(char)
            if char == '#':
                point = Point(
                    y=len(expanded_universe),
                    x=len(new_row)-1
                )
                galaxies.append(point)
        
        expanded_universe.append(new_row)
        if not galaxy_rows[y]:
            for _ in range(0,  expand_factor):
                expanded_universe.append(new_row)

    total = 0
    for start, galaxy_1 in enumerate(galaxies):
        for galaxy_2 in galaxies[start:]:
            total += find_manhattan_distance(galaxy_1, galaxy_2)
    return total


        


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