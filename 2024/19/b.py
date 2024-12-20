#!/usr/bin/python3
import functools
from collections import defaultdict
import argparse
import sys
import os

@functools.cache
def match_pattern(to_match, available):
    if len(to_match) == 0:
        return 1

    counter = 0
    for pattern in available:
        if to_match[0:len(pattern)] == pattern:
            counter += match_pattern(to_match[len(pattern):], available)
    return counter


def run(lines):
    patterns = tuple(lines[0].split(", "))

    count = 0
    for line in lines[2:]:
        count += match_pattern(line, patterns)
        
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