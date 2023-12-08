#!/usr/bin/python3
from collections import defaultdict
import argparse
import sys
import os
import re


# 3254735972 - answer was too high
map_of_maps = {}
map_of_values = defaultdict(list)

title_re = re.compile('(?P<from>\w+)-to-(?P<to>\w+) map:')
def create_map(title, numbers):
    match = title_re.match(title)
    map_from = match.group('from')
    map_to = match.group('to')

    map_of_maps[map_to] = map_from
    ranges = []

    for line in numbers:
        (dest, src, length) = [int(x) for x in line.split()]
        # sorting actually seems to break this so ignore        
        ranges.append((dest, dest + length, src - dest))
        map_of_values[map_to] = ranges


def run(lines):
    seed_line = lines[0].split(":")
    seeds = [int(x) for x in seed_line[1].split()]

    seed_pairs = []
    for x in range(0, len(seeds), 2):
        start = int(seeds[x])
        length = int(seeds[x+1])
        seed_pairs.append((start, start + length, 0))

    block = []
    for line in lines[1:]:
        if line:
            block.append(line)
        elif block:
            create_map(block[0], block[1:])
            block = []
        
    create_map(block[0], block[1:])


    # get real max 
    x = 0
    while True:
        cur_val = x
        x += 1
        cur_key = 'location'
        
        while True:
            if cur_key == 'seed':
                for seed_pair in seed_pairs:
                    if cur_val >= seed_pair[0] and cur_val <= seed_pair[1]:
                        return cur_val
            cur_map = map_of_values.get(cur_key)
            if not cur_map:
                break

            for (start, end, offset) in cur_map:
                if cur_val >= start and cur_val <= end:
                    cur_val += offset
                    break
            cur_key = map_of_maps.get(cur_key)
            # print(cur_key, cur_val)



        # for (start, end, offset) in cur_map:
        #     if cur_val >= statr and cur_val <= end:
        #         cur_val += offset
        # print(cur_key, cur_map)

    # min_location = None
    # seen = dict()
    # for seed_pair in seed_pairs:
    #     for seed in range(seed_pair[0], seed_pair[1]):
    #         cur_val = seed
    #         cur_key = 'seed'
    #         while cur_key != 'location':            
    #             for (start, end, dest_offset) in map_of_values[cur_key]:
    #                 if cur_val >= start and cur_val <= end:
    #                     cur_val += dest_offset
    #                     break
    #             cur_key = map_of_maps[cur_key]
    #         min_location = min(min_location, cur_val) if min_location is not None else cur_val
    # return min_location
        
    

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