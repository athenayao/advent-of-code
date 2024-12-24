#!/usr/bin/python3
import time
from dataclasses import dataclass
from collections import defaultdict
import argparse
import os

@dataclass
class Node:
    value: str
    connections: set

    def add_connection(self, other):
        self.connections.add(other)

    def __hash__(self):
        return hash(self.value)
    
    def __repr__(self):
        # return f"Node({self.value}) -> {[c.value for c in self.connections]}"
        return self.value
    
    def __str__(self):
        return repr(self)

def find_group(nodes, start_node):
    max_result = []
    results = set()
    
    for n1 in start_node.connections:
        c1 = set(start_node.connections)
        c1.add(start_node)
        c2 = set(n1.connections)
        c2.add(n1)
    
        common = c1 & c2
        results.add(tuple(sorted([n.value for n in common])))
        if len(common) > len(max_result):
            max_result = tuple(sorted([n.value for n in common]))
    return results

def run(lines):
    nodes = {}
    for line in lines:
        c1, c2 = line.split("-")
        if c1 in nodes:
            n1 = nodes.get(c1)
        else:
            n1 = Node(c1, set())    
            nodes[c1] = n1
        
        if c2 in nodes:
            n2 = nodes.get(c2)
        else:
            n2 = Node(c2, set())
            nodes[c2] = n2

        n1.add_connection(n2)
        n2.add_connection(n1)

    counts = defaultdict(int)
    for n in nodes.values():
        x = find_group(nodes, n)
        for value in x:
            counts[value] += 1
    
    max_result = []
    for tup, count in counts.items():
        if count != len(tup):
            continue
        if len(tup) > len(max_result):
            max_result = tup

    return ",".join(max_result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='run.py')
    parser.add_argument('-x', '--example', action='store_true')
    args = parser.parse_args()

    filename = 'input-example.txt' if args.example else 'input.txt'

    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, filename), 'r') as f:
        lines = f.read().splitlines()
        start_time = time.time()
        answer = run(lines)
        print("### ANSWER ### ")
        print(answer)
        print("--- %s seconds ---" % (time.time() - start_time))
