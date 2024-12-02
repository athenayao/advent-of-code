#!/usr/bin/python3
from collections import defaultdict
import argparse
import sys
import os

def run(lines):
    left_side = []
    right_side = []
    for line in lines:
        l, r = line.split()
        left_side.append(int(l, 10))
        right_side.append(int(r, 10))

    right_side_count = defaultdict(int)
    for number in right_side:
        right_side_count[number] += 1
    
    score = 0
    for number in left_side:
        score += number * right_side_count[number]
    return score
    



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