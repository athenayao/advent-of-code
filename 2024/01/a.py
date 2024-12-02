#!/usr/bin/python3
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
    left_side.sort()
    right_side.sort()
    sum = 0
    for idx, _ in enumerate(left_side):
        sum += abs(left_side[idx] - right_side[idx])
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