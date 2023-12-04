#!/usr/bin/python3
import argparse
import sys
import os
import re


def run(lines):
    pattern = re.compile('Card\s+(\d+): (.+) \| (.+)')
    total = 0
    for line in lines:
        print(line)
        match = pattern.match(line)
        (card_id, my_numbers, winning_numbers) = match.groups()
        my_set = set(my_numbers.split())
        winning_set = set(winning_numbers.split())

        intersect = len(my_set.intersection(winning_set))
        if intersect - 1 >= 0:
            total += 2 ** (intersect - 1)
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