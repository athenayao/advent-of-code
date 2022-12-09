import os
import re

MEM_RE = r'mem\[(\d+)\] = (.+)'
MASK_RE = r'mask = (.*)'

mask_length = 36

def parse_program(line):
    match = re.match(MEM_RE, line)
    return (int(match[1]), int(match[2]))


def convert_to_binary(number):
    as_binary = [0] * mask_length
    index = 0
    while number > 0:
        as_binary[index] = number & 1
        number = number >> 1
        index += 1
    return as_binary


def convert_to_decimal(as_binary):
    decimal = 0
    for (index, digit) in enumerate(as_binary):
        if digit == 1:
            decimal += 2**index
    return decimal

        
def get_variants(mask, binary, index):
    if index == len(mask):
        return [[]]
    
    char = mask[index]
    if char == '1':
        return [[1] + variant for variant in get_variants(mask, binary, index + 1)]
    elif char == '0':
        return [[binary[index]] + variant for variant in get_variants(mask, binary, index + 1)]
    elif char == 'X':
        variants = []
        for binary_choice in (1, 0):
            variants.extend([binary_choice] + variant for variant in get_variants(mask, binary, index + 1))
        return variants
    

def apply_mask(mask, number):
    binary = convert_to_binary(number)
    reversed_mask = list(mask)
    reversed_mask.reverse()
    variants = get_variants(reversed_mask, binary, 0)

    return [convert_to_decimal([int(v) for v in variant]) for variant in variants]


def run(lines):
    mem = {}
    for line in lines:
        match = re.match(MASK_RE, line)
        if match != None:
            mask = match[1]
            continue
        
        mem_location, value = parse_program(line)
        for masked_value in apply_mask(mask, mem_location):
            mem[masked_value] = value
    return sum(mem.values())

            
if __name__ == '__main__':
    is_example = False
    script_dir = os.path.dirname(__file__)
    filename = 'input-example.txt' if is_example else 'input.txt'
    with open(os.path.join(script_dir, filename), 'r') as f:
        lines = f.read().splitlines()
        answer = run(lines)
        print("### ANSWER ### ")
        print(answer)