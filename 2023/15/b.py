#!/usr/bin/python3
from collections import defaultdict, namedtuple
import argparse
import sys
import os

Item = namedtuple('Item', 'label, value')
def run_hash(input):
    current_value = 0
    for c in list(input):
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value

def run(lines):
    buckets = defaultdict(list)
    for input in lines[0].split(','):
        input = input.strip()
        if '-' in input:
            label = input[0:-1]
            key = run_hash(label)
            for i, item in enumerate(buckets[key]):
                if item.label == label:
                    # is this cheating
                    buckets[key].pop(i)
                    break
        else:
            label, value = input.split('=')
            key = run_hash(label)
            found = False
            for i, item in enumerate(buckets[key]):
                if item.label == label:
                    found = True
                    buckets[key][i] = Item(label, value)
                    break
            if not found:
                buckets[key].append(Item(label, value))

    total = 0
    for key in buckets.keys():
        for slot, item in enumerate(buckets[key]):
            subtotal=(int(key) + 1) * (slot + 1) * int(item.value)
            print(int(key) + 1, slot + 1, int(item.value), '=', subtotal)
            total += subtotal
    return total

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