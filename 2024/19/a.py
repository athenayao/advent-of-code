#!/usr/bin/python3
import re
import argparse
import sys
import os

def run(lines):
    patterns = lines[0].split(", ")
    patterns_group = "|".join(patterns)
    REGEX = re.compile(r"^(?:%s)+$" % patterns_group)
    count = 0
    for line in lines[2:]:
        if REGEX.match(line):
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