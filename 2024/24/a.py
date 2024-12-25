#!/usr/bin/python3
from dataclasses import dataclass
from collections import deque
import argparse
import sys
import os


def command_and(wires, in1, in2):
    v1 = wires[in1]
    v2 = wires[in2]
    if v1 == 0 or v2 == 0:
        return 0
    return 1

def command_or(wires, in1, in2):
    v1 = wires[in1]
    v2 = wires[in2]
    if v1 == 1 or v2 == 1:
        return 1
    return 0

def command_xor(wires, in1, in2):
    v1 = wires[in1]
    v2 = wires[in2]
    if v1 == v2:
        return 0
    return 1
    
commands = {
    'AND': command_and,
    'OR': command_or,
    'XOR': command_xor,
}

def get_output_bits(wires):
    zindex = 0
    output = 0
    while True:
        index_str = str(zindex).zfill(2)

        bit = wires.get(f"z{index_str}")
        if bit is None:
            return output
        # bits.append(bit)
        if bit == 1:
            output += 2 ** zindex
        zindex += 1
    

def run(lines):
    wires = {}
    mode = 'initial'
    queue = deque()

    for line in lines:
        if not line:
            mode = 'gate'
            continue
        if mode == 'initial':
            wire, initial_value = line.split(":")
            initial_value = int(initial_value)
            wires[wire] = initial_value
        elif mode == 'gate':
            in1, command, in2, _, out = line.split()
            queue.append((in1, command, in2, out))
    
    while len(queue):
        item = queue.popleft()
        in1, command, in2, out = item
        if in1 in wires and in2 in wires:
            wires[out] = commands[command](wires, in1, in2)
        else:
            queue.append(item)

    return(get_output_bits(wires))

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