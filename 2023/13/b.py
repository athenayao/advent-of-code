#!/usr/bin/python3
import argparse
import sys
import os

def check_vertical_reflection(pattern, start, override_y, override_x, new_value):
    counter = 0

    while True:
        up_ = start - counter
        down_ = start + counter + 1

        if up_ < 0:
            return start + 1
        if down_ > len(pattern) - 1:
            return start + 1 

        if override_y == up_:
            up_pattern = pattern[up_][:override_x] + new_value + pattern[up_][override_x+1:]
        else:
            up_pattern = pattern[up_]

        if override_y == down_:
            down_pattern = pattern[down_][:override_x] + new_value + pattern[down_][override_x+1:]
        else:
            down_pattern = pattern[down_]
        if up_pattern == down_pattern:
            counter += 1
        else:
            return -1

# too low: 28458
# too high: 50584
def process_patterns(base_pattern):
    original_answer = process_pattern(base_pattern)

    for y, row in enumerate(base_pattern):
        for x, cell in enumerate(list(row)):
            new_value = '.' if cell == '#' else '#'
            index = process_pattern(base_pattern, y, x, new_value)
            if index != -1 and index != original_answer:
                return index

    # what if I just rotate the grid
    # this is probably possible with just math and not writing
    # my bug is probably in this rotation code
    grid = [[] for _ in range(0, len(base_pattern[0]))]
    for i, line in enumerate(base_pattern):
        for j, char in enumerate(list(line)):
            grid[j].append(char)
    
    rotated_pattern = [''.join(line) for line in grid]

    for y, row in enumerate(rotated_pattern):
        for x, cell in enumerate(list(row)):
            new_value = '.' if cell == '#' else '#'
            index = process_pattern(rotated_pattern, y, x, new_value)
            if index != -1 and index != original_answer:
                return index
    

    if index == -1:
        print("could not handle")
        print("\n".join(base_pattern))
    return index

            
def process_pattern(pattern, override_y=None, override_x=None, override_value=None):
    # maybe we can be smarter about this, we know most of the lines won't change...
    for start in range(0, len(pattern) - 1):
        index = check_vertical_reflection(pattern, start, override_y, override_x, override_value)
        if index != -1:
            return 100 * index



    return -1



def run(lines):
    pattern = []

    total = 0
    for line in lines:
        if line == '':
            total += process_patterns(pattern)
            pattern = []
        else:
            pattern.append(line)
    total += process_patterns(pattern)
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