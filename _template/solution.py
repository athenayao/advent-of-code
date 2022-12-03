#! python3
from optparse import OptionParser
import sys

def run_part_1(filename):
    with open(filename, 'r') as file:
        for raw_line in file.readlines():
            line = raw_line.strip()
            print(".." + line)
            # do something


def run_part_2(filename):
    with open(filename, 'r') as file:
        for raw_line in file.readlines():
            line = raw_line.strip()
            print(".." + line)
            # do something


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