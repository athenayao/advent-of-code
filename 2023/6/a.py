#!/usr/bin/python3
import argparse
import sys
import os

def calculate_travel(hold, max_time):
    return ((max_time - hold) * hold)


def run(lines):
    times = [int(x) for x in lines[0].split(":")[1].split()]
    distances = [int(x) for x in lines[1].split(":")[1].split()]
    result = 1
    for (time, min_distance) in zip(times, distances):
        num_ways = 0
        # wonder if I should bisect...
        # ooh linear bell curve. but I'll be lazy
        for t in range(1, time):
            if calculate_travel(t, time) > min_distance:
                num_ways += 1
        result *= num_ways
    return result



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