#!/usr/bin/python3
import argparse
import sys
import os

def run_hash(input):
    current_value = 0
    for c in list(input):
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value

def run(lines):
    total = 0
    for input in lines[0].split(','):
        total += run_hash(input.strip())
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