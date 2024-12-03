#!/usr/bin/python3
import argparse
import sys
import os
import re

MUL_RE = re.compile(r'mul\((\d+),(\d+)\)')

def run(lines):
    sum = 0
    line = "".join(lines)
    pos = 0
    is_start = True
    while match := MUL_RE.search(line, pos):
        pos = match.start() + 1
        is_enabled = False
        if is_start:
            is_enabled = True
            is_start = False
        else:
            last_do = line[0:pos].rfind('do()')
            last_dont = line[0:pos].rfind('don\'t()')
            is_enabled = last_do > last_dont
        if is_enabled:
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