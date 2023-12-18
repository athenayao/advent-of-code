#!/usr/bin/python3
import argparse
import sys
import os
import re

LINE_REGEX = re.compile('#(?P<hex>[a-f0-9]{5})(?P<direction>\d)')

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __hash__(self):
        return hash((self.x, self.y))


directions = {
    'R': Point(1, 0),
    'L': Point(-1, 0),
    'U': Point(0, -1),
    'D': Point(0, 1),
}

dir_map = ['R', 'D', 'L', 'U']

def shoelace(vertices):
    # gauss' shoelace formula
    total = 0
    for i, point in enumerate(vertices):
        next_i = (i+1) % len(vertices)
        subtotal = (vertices[i].x * vertices[next_i].y) - (vertices[i].y * vertices[next_i].x) 
        # print(subtotal, vertices[i], vertices[next_i])
        total += subtotal
 
    return total // 2

def run(lines):
    vertices = []

    point = Point(0, 0)

    border = 0
    for line in lines:
        match = LINE_REGEX.search(line)
        direction = directions[dir_map[int(match.group('direction'))]]
        times = int(match.group('hex'), 16)
        border += times

        new_point = Point(direction.x * times + point.x, direction.y * times + point.y)
        point = new_point
        vertices.append(point)
    
    return shoelace(vertices) + border // 2 + 1
    

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