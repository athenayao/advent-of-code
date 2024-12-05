#!/usr/bin/python3
import argparse
import sys
import os

class Node:
    def __init__(self, label):
        self.label = label
        self.connections = set()
    
    def add_connection(self, connection):
        self.connections.add(connection)

    def __repr__(self):
        star = " *" if self.label in set(["hfx", "pzl", "bvb", "cmg", "nvd", "jqt"]) else ""
        return f'{self.label} -> {self.connections}{star}'

def run(lines):
    all_nodes = set()
    tmp = {}
    nodes = {}

    for line in lines:
        left, right = line.split(":")

        right_arr = [n.strip() for n in right.split()]
        labels = [left, *right_arr]
        for label in labels:
            if label not in nodes:
                nodes[label] = Node(label)
        tmp[left] = right_arr
    
    for (left, right) in tmp.items():
        for label in right:
            nodes[left].add_connection(label)
            nodes[label].add_connection(left)
    print("\n".join([str(node) for node in nodes.values()]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='run.py')
    parser.add_argument('-x', '--example', action='store_true')
    args = parser.parse_args()

    filelabel = 'input-example.txt' if args.example else 'input.txt'

    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, filelabel), 'r') as f:
        answer = run(f.read().splitlines())
        print("### ANSWER ### ")
        print(answer)