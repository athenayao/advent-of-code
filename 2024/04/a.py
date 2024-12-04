#!/usr/bin/python3
import argparse
import enum
import sys
import os

grid = []
new_grid = []

def print_grid(grid):
    print( "\n".join(["".join(row) for row in grid]))

def find_xmas(grid, row, col):
    found = 0
    for row_delta in range(-1, 2):
        if row + (3 * row_delta) < 0 or row + (3 * row_delta) >= len(grid):
            continue

        for col_delta in range(-1, 2):
            if col + (3 * col_delta) < 0 \
                or col + (3 * col_delta) >= len(grid[row]) \
                or (row_delta == 0 and col_delta == 0):
                continue

            if grid[row][col] == 'X' \
                and grid[row+row_delta][col+col_delta] == 'M' \
                and grid[row+(row_delta * 2)][col + (col_delta*2)] == 'A' \
                and grid[row+(row_delta * 3)][col + (col_delta*3)] == 'S':

                new_grid[row][col] = 'X'
                new_grid[row + row_delta][col+col_delta] = 'M'
                new_grid[row+(row_delta * 2)][col + (col_delta*2)] = 'A'
                new_grid[row+(row_delta * 3)][col + (col_delta*3)] = 'S'
                found += 1
            
    return found

            
    
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
            if col == 'X':
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