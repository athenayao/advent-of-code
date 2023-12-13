#!/usr/bin/python3
import argparse
import sys
import os

def check_vertical_reflection(pattern, start):
    counter = 0

    while True:
        up_ = start - counter
        down_ = start + counter + 1

        if up_ < 0:
            return start + 1
        if down_ > len(pattern) - 1:
            return start + 1 

        if pattern[up_] == pattern[down_]:
            counter += 1
        else:
            return -1
    
def process_pattern(pattern):
    for start in range(0, len(pattern) - 1):
        index = check_vertical_reflection(pattern, start)
        if index != -1:
            return 100 * index


    # what if I just rotate the grid
    # this is probably possible with just math and not writing
    grid = [[] for _ in range(0, len(pattern[0]))]
    for i, line in enumerate(pattern):
        for j, char in enumerate(list(line)):
            grid[j].append(char)

    pattern2 = [''.join(line) for line in grid]
    for start in range(0, len(pattern2) - 1):
        index = check_vertical_reflection(pattern2, start)
        if index != -1:
            return index

    print("\ndid not work for pattern1\n", '\n'.join(pattern))
    print("\ndid not work for pattern2\n", '\n'.join(pattern2))
    return 0



def run(lines):
    pattern = []

    total = 0
    for line in lines:
        if line == '':
            total += process_pattern(pattern)
            pattern = []
        else:
            pattern.append(line)
    total += process_pattern(pattern)
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