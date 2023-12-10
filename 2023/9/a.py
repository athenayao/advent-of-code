#!/usr/bin/python3
import argparse
import sys
import os

def find_diffs(numbers, depth=0):
    new_diff = []
    all_zeroes = True
    for i in range(0, len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]
        new_diff.append(diff)
        if diff != 0:
            all_zeroes = False

    if all_zeroes:
        return numbers[i]
    
    return find_diffs(new_diff, depth=depth+1) + numbers[-1]




def run(lines):
    total = 0
    for line in lines:
        numbers = [int(n) for n in line.split()]
        total += find_diffs(numbers)
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