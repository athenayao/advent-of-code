#! python3
from optparse import OptionParser
import sys

def calculate_priority(value):
    if value.isupper():
        value = ord(value) - (64 - 26)
    else:
        value = ord(value) - 96
    return value

def run_part_1(filename):
    with open(filename, 'r') as file:
        total = 0
        for raw_line in file.readlines():
            line = raw_line.strip()
            halfway = int(len(line) /2)
            set_1 = set(line[0:halfway])
            set_2 = set(line[halfway:])
            intersect = set_1.intersection(set_2)
            value = ''.join(intersect)
            total += value
        print(total)


def run_part_2(filename):
    with open(filename, 'r') as file:
        lines = []
        total = 0
        for raw_line in file.readlines():
            line = raw_line.strip()
            lines.append(set(line))

            if len(lines) == 3:
                result_set = lines[0].intersection(lines[1]).intersection(lines[2])
                total += calculate_priority(''.join(result_set))
                lines = []
        print(total)   


if __name__ == '__main__':
    mode = sys.argv[1]
    if not mode:
        mode == "1a"

    if mode == "1a":
        run_part_1('./sample-input.txt')
    elif mode == "1b":
        run_part_1("./input.txt")
    elif mode == "2a":
        run_part_2('./sample-input.txt')
    else:
        run_part_2('./input.txt')