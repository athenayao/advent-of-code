#!/usr/bin/python3
import argparse
import enum
import sys
import os

grid = []
new_grid = []

def print_grid(grid):
    print( "\n".join(["".join(row) for row in grid]))

valid_chars = set(['M', 'S'])
def find_xmas(grid, row, col):
    # only need to look at the four corners

    # but also boundaries
    if row == 0 or row == len(grid) - 1 or col == 0 or col == len(grid[row]) - 1:
        return 0

    left_slash = set([grid[row-1][col+1], grid[row+1][col-1]])
    right_slash = set([grid[row-1][col-1], grid[row+1][col+1]])
    if left_slash == valid_chars and right_slash == valid_chars:
        return 1

    return 0

            
    
def run(lines):
    for row_index, row in enumerate(lines):
        grid.append([])
        new_grid.append([])
        for col_index, cell in enumerate(row):
            grid[row_index].append(cell)
            new_grid[row_index].append('.')

    found = 0    
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if col == 'A':
                found += find_xmas(grid, row_index, col_index)
    
    return found
        
                
                    



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