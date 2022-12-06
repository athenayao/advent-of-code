#! python3
import sys

def find_marker(string, length):
    for i in range(0, len(string) - length - 1):
        unique = set(string[i:i+length])
        if len(unique) == length:
            return i + length

def run_part_1(filename):
    with open(filename, 'r') as file:
        for raw_line in file.readlines():
            line = raw_line.strip()
            print(find_marker(line, 4))


def run_part_2(filename):
    with open(filename, 'r') as file:
        for raw_line in file.readlines():
            line = raw_line.strip()
            print(find_marker(line, 14))



if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else None
    if not mode:
        mode == "ax"

    if mode == "ax":
        run_part_1("./sample-input.txt")
    elif mode == "a":
        run_part_1('./input.txt')
    elif mode == "bx":
        run_part_2("./sample-input.txt")
    elif mode == "b":
        run_part_2("./input.txt")