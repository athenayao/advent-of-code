#!/usr/bin/python3
from collections import defaultdict
import argparse
import sys
import os

counter = 0
def match_pattern(to_match, available):
    global counter
    if len(to_match) == 0:
        counter += 1
        return

    for pattern in available:
        if to_match[0:len(pattern)] == pattern:
            match_pattern(to_match[len(pattern):], available)


def run(lines):
    patterns = lines[0].split(", ")

    for line in lines[2:]:
        match_pattern(line, patterns)
        
    global counter
    return counter

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