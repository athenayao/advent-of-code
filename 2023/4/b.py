#!/usr/bin/python3
import argparse
from collections import defaultdict
import sys
import os
import re
    
def run(lines):
    pattern = re.compile('Card\s+(\d+): (.+) \| (.+)')
    processed = 0

    counts = defaultdict(lambda: 1)
    for line in lines:
        match = pattern.match(line)
        (card_id, my_numbers, winning_numbers) = match.groups()
        card_id = int(card_id)
        my_set = set(my_numbers.split())
        winning_set = set(winning_numbers.split())

        intersect = len(my_set.intersection(winning_set))

        counts[card_id] += 0
        for x in range(card_id + 1, card_id + intersect + 1):
            counts[x] += counts[card_id]
    return sum(counts.values())


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