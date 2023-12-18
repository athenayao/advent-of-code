#!/usr/bin/python3
import argparse
import sys
import os

def print_grid(grid):
    print('\n'.join(''.join(line) for line in grid))
# is this djikstra's or is it moot because of the direction conditions?
def run(lines):
    grid = []
    for y, line in enumerate(lines):
        grid.append([])
        for x, cell in enumerate(line):
            grid[y].append(cell)

    print_grid(grid)

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