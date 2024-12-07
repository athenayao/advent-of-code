#!/usr/bin/python3
import argparse
import sys
import os


def mul(expected_result, total_so_far, numbers):
    total_so_far *= numbers[0]
    return find_equations(expected_result, total_so_far, numbers[1:])

def sum(expected_result, total_so_far, numbers):
    total_so_far += numbers[0]
    return find_equations(expected_result, total_so_far, numbers[1:])

def concat(expected_result, total_so_far, numbers):
    total_so_far = int(str(total_so_far) + str(numbers[0]))
    return find_equations(expected_result, total_so_far, numbers[1:])

def find_equations(expected_result, total_so_far, numbers):
    if len(numbers) == 0:
        return total_so_far == expected_result
    
    return sum(expected_result, total_so_far, numbers) or mul(expected_result, total_so_far, numbers) or concat(expected_result, total_so_far, numbers)

def run(lines):
    valid_sum = 0
    for line in lines:
        test_value, numbers_raw = line.split(":")
        test_value = int(test_value)
        numbers = [int(x) for x in numbers_raw.split()]
        
        is_valid = find_equations(test_value, 0, numbers)
        if is_valid:
            valid_sum += test_value
    return valid_sum

        

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