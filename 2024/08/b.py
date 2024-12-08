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


def find_antinodes(p1, p2, max_x, max_y):
    x_diff = p2.x - p1.x
    y_diff = p2.y - p1.y

    antinodes = [p1, p2]

    negative_point = p1
    # going negative
    while True:
        new_x = negative_point.x - x_diff
        new_y = negative_point.y - y_diff
        if new_x < 0 or new_x > max_x:
            break
        if new_y < 0 or new_y > max_y:
            break
        negative_point = Point(new_x, new_y)
        antinodes.append(negative_point)


    positive_point = p2
    # going negative
    while True:
        new_x = positive_point.x + x_diff
        new_y = positive_point.y + y_diff
        if new_x < 0 or new_x > max_x:
            break
        if new_y < 0 or new_y > max_y:
            break

        positive_point = Point(new_x, new_y)
        antinodes.append(positive_point)

    return antinodes


def run(lines):
    points = defaultdict(list)
    for row_idx, row in enumerate(lines):
        for col_idx, value in enumerate(row):
            if not CHAR_REGEX.match(value):
                continue
            points[value].append(Point(col_idx, row_idx))

    max_y = row_idx
    max_x = col_idx
    
    antinodes = set()
    for key, p in points.items():
        for p_index, p0 in enumerate(p):
            for p1 in p[p_index+1:]:
                antinodes.update(find_antinodes(p0, p1, max_x, max_y))

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