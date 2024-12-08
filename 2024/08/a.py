#!/usr/bin/python3
import re
import math
from dataclasses import dataclass
from collections import defaultdict
import argparse
import sys
import os

CHAR_REGEX = re.compile(r'[a-zA-Z0-9]')

@dataclass(frozen=True)
class Point():
    x: int
    y: int


def find_antinodes(p1, p2):
    print(p1, p2)
    x_diff = p2.x - p1.x
    y_diff = p2.y - p1.y

    p0 = Point(p1.x - x_diff, p1.y - y_diff)
    p3 = Point(p2.x + x_diff, p2.y + y_diff)

    return [p0, p3]


def line_from_points(p1, p2):
    # y = mx + b
    slope = (p2.y - p1.y) / (p2.x - p1.x)
    y_intercept = p1.y - slope * p1.x
    return(slope, y_intercept)


def run(lines):
    points = defaultdict(list)
    for row_idx, row in enumerate(lines):
        for col_idx, value in enumerate(row):
            if not CHAR_REGEX.match(value):
                continue
            points[value].append(Point(col_idx, row_idx))

    max_row_idx = row_idx
    max_col_idx = col_idx
    
    antinodes = set()
    for key, p in points.items():
        for p_index, p0 in enumerate(p):
            for p1 in p[p_index+1:]:
                antinodes.update([antinode for antinode in find_antinodes(p0, p1) if antinode.x >= 0 and antinode.x <= max_col_idx and antinode.y >= 0 and antinode.y <= max_row_idx])

    print(antinodes)
    return len(antinodes)

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