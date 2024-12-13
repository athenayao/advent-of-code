#!/usr/bin/python3
import math
import re
import argparse
import sys
import os

def do_math(a_x, a_y, b_x, b_y, p_x, p_y):
    a_lcm = math.lcm(a_x, a_y)

    a_lcm_x = a_lcm / a_x
    a_lcm_y = a_lcm / a_y

    ps = a_lcm_x * p_x - a_lcm_y * p_y
    b_num = ps / (a_lcm_x * b_x - a_lcm_y * b_y )
    a_num = (p_x - b_x * b_num) / a_x

    return (a_num, b_num)    



LINE_REGEX = re.compile(r'(?:.+): X[+=](?P<x>\d+), Y[+=](?P<y>\d+)')
def run(lines):
    num_tokens = 0
    line_iter = iter(lines)
    while True:
        match = LINE_REGEX.match(next(line_iter))
        g = match.groupdict()
        a_x = int(g['x'])
        a_y = int(g['y'])

        match = LINE_REGEX.match(next(line_iter))
        g = match.groupdict()
        b_x = int(g['x'])
        b_y = int(g['y'])

        match = LINE_REGEX.match(next(line_iter))
        g = match.groupdict()
        p_x = int(g['x'])
        p_y = int(g['y'])

        # blank or StopIter
        try:
            next(line_iter)
        except:
            break
        
        (a_num, b_num) = do_math(a_x, a_y, b_x, b_y, p_x, p_y)
        if not a_num.is_integer():
            continue
        if not b_num.is_integer():
            continue

        this_token = a_num * 3 + b_num

        num_tokens += this_token

    return int(num_tokens)


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