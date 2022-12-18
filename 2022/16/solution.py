#! python3
import sys
import re

INPUT_REGEX = r'Valve ([A-Z]{2}) has flow rate=(\d+); tunnel.* valves? (.*)'

class Valve:
    def __init__(self, name, rate, connections):
        self.name = name
        self.rate = int(rate)
        self.connections = [node.strip() for node in connections.split(',')]
        self.open = False

    def __repr__(self):
        connections = ' '.join(self.connections)
        is_open = 'o' if self.open else 'x'
        return f'{is_open} {self.name} -> ({connections})'

def traverse(node, seen):
    seen = set(seen)

    while len(node.connections):
        c = node.connections.pop()


def run_part_1(filename):
    valves = {}
    with open(filename, 'r') as file:
        for raw_line in file.readlines():
            line = raw_line.strip()
            match = re.match(INPUT_REGEX, line)

            valve = Valve(match[1], match[2], match[3])
            valves[valve.name] = valve
        
        # dfs
        seen = set()

        # TODO: add some sort of weight by distance??
        valve = valves['AA']
        minute = 0
        while True:
            minute += 1

                

            seen.add(valve.name)


            


def run_part_2(filename):
    with open(filename, 'r') as file:
        for raw_line in file.readlines():
            line = raw_line.strip()
            print(".." + line)
            # do something


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else None
    if not mode:
        mode == "ax"

    if mode == "ax":
        run_part_1('./example.txt')
    elif mode == "a":
        run_part_1("./input.txt")
    elif mode == "bx":
        run_part_2('./example.txt')
    elif mode == "b":
        run_part_2('./input.txt')
        