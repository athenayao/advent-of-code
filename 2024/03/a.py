#!/usr/bin/python3
import argparse
import sys
import os
import re

MUL_RE = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
def run(lines):
    line = lines[0]
    pos = 0
    sum = 0
    while match := MUL_RE.search(line, pos):
        sum += int(match.groups()[0], 10) * int(match.groups()[1], 10)
        pos = match.start() + 1
    return sum
        
    

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