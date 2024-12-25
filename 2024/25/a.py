#!/usr/bin/python3
import argparse
import sys
import os


def parse_block(block):
    parsed_heights = [None] * len(block[0])
    parsed = 0
    
    if block[0] == '#####':
        # this is a lock
        type_ = 'lock'
    else:
        # this is a key
        type_ = 'key'

    for row_num, line in enumerate(block):
        for index, value in enumerate(line):
            if parsed_heights[index] is not None:
                continue

            if type_ == 'lock' and value == '.':
                parsed_heights[index] = row_num - 1
                parsed += 1
            elif type_ == 'key' and value == '#':
                parsed_heights[index] = row_num
                parsed += 1

            if parsed == 5:
                return (type_, parsed_heights)

def run(lines):
    keys = []
    locks = []

    block = []
    for line in lines:
        if not line:
            type_, heights = parse_block(block)
            if type_ == 'lock':
                locks.append(heights)
            else:
                keys.append(heights)
            block = []
        else: 
            block.append(line)
    type_, heights = parse_block(block)
    if type_ == 'lock':
        locks.append(heights)
    else:
        keys.append(heights)
    
    max_block_height = len(block)
    
    count = 0
    for lock in locks:
        for key in keys:
            print(lock, key)
            did_overlap = False
            for (h1, h2) in zip(lock, key):
                print(h1, h2, max_block_height)
                if h1 >= h2:
                    did_overlap = True
                    break
            if not did_overlap:    
                count += 1
    return count


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