#!/usr/bin/python3
import argparse
import sys
import os
import re

MUL_RE = re.compile(r'mul\((\d+),(\d+)\)')
DO_DONT_RE = re.compile(r'(do\(\)|don\'t\(\))')

def run(lines):
    sum = 0
    line = "".join(lines)

    enabled_at = [0]
    
    dd_pos = 0
    is_enabled = True
    the_match = None
    while match:= DO_DONT_RE.search(line, dd_pos):
        for _ in range(dd_pos, match.start()):
            enabled_at.append(is_enabled)
        is_enabled = match.groups()[0] == 'do()'
        dd_pos = match.start() + 1
        the_match = match

    for _ in range(the_match.start(), len(line)+1):
        enabled_at.append(is_enabled)

    pos = 0
    while match := MUL_RE.search(line, pos):
        pos = match.start() + 1
        if enabled_at[pos]:
            sum += int(match.groups()[0], 10) * int(match.groups()[1], 10)

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