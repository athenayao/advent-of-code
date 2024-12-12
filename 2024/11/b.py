#!/usr/bin/python3
import argparse
import os

def update_stone(stone):
    if stone == 0:
        return [1]

    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        return [int(stone_str[:len(stone_str) // 2]), int(stone_str[len(stone_str) // 2:])]

    return [stone * 2024]


def blink(stones):
    new_stones = []
    for stone in stones:
        new_stones += update_stone(stone)
    return new_stones

def run(lines):
    stones = [int(x) for x in lines[0].split()]
    print(stones)

    for i in range(0, 25):
        stones = blink(stones)
    return len(stones)
    

    

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