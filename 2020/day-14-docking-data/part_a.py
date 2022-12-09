import os
import re

MEM_RE = r'mem\[(\d+)\] = (.+)'
MASK_RE = r'mask = (.*)'

mask_length = 36

def parse_mask(raw_mask):
    mask = {}
    for (index, char) in enumerate(reversed(raw_mask)):
        if char == '1':
            mask[index] = 1
        elif char == '0':
            mask[index] = 0
    return mask


def parse_program(line):
    match = re.match(MEM_RE, line)
    return (int(match[1]), int(match[2]))

def apply_mask(mask, number):
    as_binary = [0] * mask_length

    index = 0
    while number > 0:
        as_binary[index] = number & 1
        number = number >> 1
        index += 1

    for (key, bit_value) in mask.items():
        as_binary[key] = bit_value

    decimal = 0
    for (index, digit) in enumerate(as_binary):
        if digit == 1:
            decimal += 2**index
    return decimal


def run(lines):
    mem = {}
    for line in lines:
        match = re.match(MASK_RE, line)
        if match != None:
            mask = parse_mask(match[1])
            continue
        
        mem_location, value = parse_program(line)
        mem[mem_location] = apply_mask(mask, value)
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