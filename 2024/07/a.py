#!/usr/bin/python3
import argparse
import sys
import os


def find_max(numbers):
    max_possible = 1
    for number in numbers:
        max_possible *= number
    return max_possible

def find_min(numbers):
    min_possible = 0
    for number in numbers:
        min_possible += number
    return min_possible


def mul(expected_result, total_so_far, numbers):
    if not numbers:
        return total_so_far == expected_result
    
    total_so_far *= numbers[0]
    if mul(expected_result, total_so_far, numbers[1:]):
        return True
    elif sum(expected_result, total_so_far, numbers[1:]):
        return True
    return concat(expected_result, total_so_far, numbers[1:])

def sum(expected_result, total_so_far, numbers):
    if len(numbers) == 0:
        return total_so_far == expected_result
    
    total_so_far += numbers[0]
    if sum(expected_result, total_so_far, numbers[1:]):
        return True
    elif mul(expected_result, total_so_far, numbers[1:]):
        return True
    return concat(expected_result, total_so_far, numbers[1:])


def concat(expected_result, total_so_far, numbers):
    if len(numbers) == 0:
        return total_so_far == expected_result
    
    total_so_far = int('' + total_so_far + numbers[0])
    if sum(expected_result, total_so_far, numbers[1:]):
        return True
    elif mul(expected_result, total_so_far, numbers[1:]):
        return True
    return concat(expected_result, total_so_far, numbers[1:])

def run(lines):
    valid_sum = 0
    for line in lines:
        test_value, numbers_raw = line.split(":")
        test_value = int(test_value)
        numbers = [int(x) for x in numbers_raw.split()]
        max_possible = find_max(numbers)
        min_possible = find_min(numbers)
        
        # if test_value < min_possible or test_value > max_possible:
        #     continue
        
        # if test_value == min_possible or test_value == max_possible:
        #     valid_sum += test_value
        #     continue
        
        print("now evaluating", test_value, numbers)
        is_valid = sum(test_value, 0, numbers) or mul(test_value, 0, numbers)
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