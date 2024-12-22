#!/usr/bin/python3
import argparse
import sys
import os


def next_secret_number(secret_number):
    secret_number = mix(secret_number, secret_number << 6)
    secret_number = prune(secret_number)
    
    secret_number = mix(secret_number, secret_number >> 5)
    secret_number = prune(secret_number)

    secret_number = mix(secret_number, secret_number << 11)
    secret_number = prune(secret_number)

    return secret_number


def prune(secret_number):
    return secret_number  & (2**24 - 1)

def mix(n1, n2):
    return n1 ^ n2

def run(lines):
    sum = 0
    for line in lines:
        secret_number = int(line)
        for _ in range(0, 2000):
            secret_number = next_secret_number(secret_number)
        sum += secret_number
    return sum

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