#!/usr/bin/python3
import argparse
import sys
import os
import re

NODE_REGEX = re.compile('(?P<name>\w+) = \((?P<left>\w+), (?P<right>\w+)\)')


class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right
    
    def get_next(self, direction):
        if direction == 'L':
            return self.left
        return self.right

    @classmethod
    def parse(cls, definition):
        match = NODE_REGEX.match(definition)
        return cls(match.group('name'), match.group('left'), match.group('right'))

    def __repr__(self):
        return self.name

def run(lines):
    directions = list(lines[0])

    nodes = {}

    for line in lines[2:]:
        node = Node.parse(line)
        nodes[node.name] = node
    
    node = nodes.get('AAA')
    index = 0
    count = 0
    while node.name != 'ZZZ':
        count += 1
        next_name = node.get_next(directions[index])
        node = nodes[next_name]
        index = (index + 1) % len(directions)
    return count

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