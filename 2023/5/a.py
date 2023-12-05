#!/usr/bin/python3
from collections import defaultdict
import argparse
import sys
import os
import re


map_of_maps = {}
map_of_values = defaultdict(list)

title_re = re.compile('(?P<from>\w+)-to-(?P<to>\w+) map:')
def create_map(title, numbers):
    match = title_re.match(title)
    map_from = match.group('from')
    map_to = match.group('to')

    map_of_maps[map_from] = map_to
    ranges = []

    # make a list of from ranges
    for line in numbers:
        (dest, src, length) = [int(x) for x in line.split()]
        # do we need to append ranges
        
        ranges.append((src, src+length, dest - src))
        map_of_values[map_from] = ranges


def run(lines):
    seed_line = lines[0].split(":")
    seeds = [int(x) for x in seed_line[1].split()]

    block = []
    for line in lines[1:]:
        if line:
            block.append(line)
        elif block:
            create_map(block[0], block[1:])
            block = []
        
    create_map(block[0], block[1:])

    min_location = None
    for seed in seeds:
        # make a loop
        cur_val = seed
        cur_key = 'seed'
        while cur_key != 'location':
            # import pdb; pdb.set_trace()
            for (start, end, dest_offset) in map_of_values[cur_key]:
                if cur_val >= start and cur_val <= end:
                    cur_val += dest_offset
                    break
            cur_key = map_of_maps[cur_key]
        min_location = min(min_location, cur_val) if min_location is not None else cur_val
    return min_location
    
    

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