#!/usr/bin/python3
from collections import defaultdict
import argparse
import sys
import os

def run(lines):
    connections = defaultdict(set)
    for line in lines:
        c1, c2 = line.split("-")
        connections[c1].add(c2)
        connections[c2].add(c1)
    
    seen = set()
    for c1 in connections.keys():
        if c1.startswith('t'):
            connection_list_2 = connections.get(c1)
            for c2 in connection_list_2:
                connection_list_3 = connections.get(c2)
                for c3 in connection_list_3:
                    if c1 in connections.get(c3):
                        current = sorted([c1, c2, c3])
                        seen.add(tuple(current))
    return len(seen)

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