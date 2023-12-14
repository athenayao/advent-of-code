#!/usr/bin/python3
import argparse
import sys
import os

ROUND = 'O'
CUBE = '#'
GROUND = '.'

# north, west, south, east
def roll(array, start):
    cur_index = start
    char = array[cur_index]
    next_index = cur_index - 1
    next_char = array[next_index]

    if char != ROUND:
        return

    while (next_char == GROUND) and cur_index > 0:
        # roll it backwards
        array[next_index] = ROUND
        array[cur_index] = GROUND
    
        cur_index -= 1
        next_index = cur_index - 1
        next_char = array[next_index]

    return


def rotate(lines):
    grid = [list() for _ in range(0, len(lines[0]) + 1)]
    for y, line in enumerate(lines):
        for x, cell in enumerate(line):
            grid[x].append(cell)
    return grid

def run(lines):
    # north, west, south, east
    grid = lines
    for i in range(0, 5):
        grid = rotate(grid)

        # total = 0    
        for line in grid:
            for i, _ in enumerate(line):
                if i == 0:
                    continue
                roll(line, i)
        print('\n'.join([''.join(line) for line in grid]))
    print('\n'.join([''.join(line) for line in grid]))
        # import pdb; pdb.set_trace()
        # subtotal = sum([len(line) - i for i, char in enumerate(line) if char == ROUND])
        # print(subtotal, ''.join(line))
        # total += subtotal
    # return total


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