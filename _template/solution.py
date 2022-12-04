#! python3
import sys

def run_part_a(filename):
    with open(filename, 'r') as file:
        for raw_line in file.readlines():
            line = raw_line.strip()
            print(".." + line)
            # do something


def run_part_b(filename):
    with open(filename, 'r') as file:
        for raw_line in file.readlines():
            line = raw_line.strip()
            print(".." + line)
            # do something


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else None
    if not mode:
        mode == "ax"

    if mode == "ax":
        run_part_a('./sample-input.txt')
    elif mode == "a":
        run_part_a("./input.txt")
    elif mode == "bx":
        run_part_b('./sample-input.txt')
    elif mode == "b":
        run_part_b('./input.txt')