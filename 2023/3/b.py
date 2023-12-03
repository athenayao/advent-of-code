#!/usr/bin/python3
from collections import defaultdict
import argparse
import sys
import os

digits = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
# but I also need to account for the same number being with multiple symbols

def adjacent_ids(symbol, number_grid):
    (sym_y, sym_x) = symbol
    seen_ids = set()
    for x in range(sym_x - 1, sym_x + 2):
        for y in range(sym_y - 1, sym_y + 2):
            number = number_grid[y].get(x)
            if number is not None:
                seen_ids.add(number)
    return seen_ids

    
def run(lines):
    id_to_value = dict()
    numbers = defaultdict(dict)
    symbols = []
    current_number = None
    current_start = None

    current_id = 0
    for (i, raw_line) in enumerate(lines):
        for (j, char) in enumerate(list(raw_line + '.')):
            if char in digits:
                if current_start is None:
                    current_number = []
                    current_start = j
                current_number.append(char)
            else:
                if current_start is not None:
                    current_end = j

                    num_str = "".join(current_number)

                    for x in range(current_start, current_end):
                        id_to_value[current_id] = int(num_str)
                        numbers[i][x] = current_id
                    current_id += 1

                    current_number = []
                    current_start = None
                    current_end = None
                if char != '*':
                    continue
            
                else:
                    symbols.append((i, j))
    
    total = 0
    for symbol in symbols:
         adjacent = adjacent_ids(symbol, numbers)
         if len(adjacent) == 2:
            gear_ratio = 1
            for x in adjacent:
                gear_ratio *= id_to_value[x]
            print(gear_ratio)
            total += gear_ratio
        
    
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