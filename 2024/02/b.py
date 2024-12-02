#!/usr/bin/python3
import argparse
import sys
import os

def check_safe(levels, skip_level):
    count_signs = {1: 0, -1: 0}

    prev_level = None
    for index, level in enumerate(levels):
        if index == skip_level:
            continue
    
        if prev_level is None:
            prev_level = level
            continue

        diff = prev_level - level
        abs_diff = abs(diff)

        if abs_diff == 0 or abs_diff > 3:
            return False

        count_signs[abs_diff // diff] += 1
        if count_signs[-1] > 0 and count_signs[1] > 0:
            return False
        
        prev_level = level
    return True

def run(reports):
    sum = 0
    for report in reports:
        levels = [int(x) for x in report.split()]
        if check_safe(levels, None):
            sum += 1
        else:
            for idx, lvl in enumerate(levels):
                if check_safe(levels, idx):
                    sum += 1
                    break
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