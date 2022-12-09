#! python3
import sys

def run_part_a(filename):
    with open(filename, 'r') as file:
        count = 0
        for raw_line in file.readlines():
            line = raw_line.strip()
            first, second = line.split(",")
            first_start, first_end = [int(x) for x in first.split("-")]
            second_start, second_end = [int(x) for x in second.split("-")]

            if (second_start <= first_start and second_end >= first_end) or (first_start <= second_start and first_end >= second_end):
                count += 1

        print(count)


def run_part_b(filename):
    with open(filename, 'r') as file:
        count = 0
        for raw_line in file.readlines():
            line = raw_line.strip()
            first, second = line.split(",")
            first_start, first_end = [int(x) for x in first.split("-")]
            second_start, second_end = [int(x) for x in second.split("-")]

            if (first_start <= second_start <= first_end) \
                or (second_start <= first_start <= second_end):
                count += 1
        print(count)


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else None
    if not mode:
        mode == "1x"

    if mode == "1x":
        run_part_a('./sample-input.txt')
    elif mode == "1":
        run_part_a("./input.txt")
    elif mode == "2x":
        run_part_b('./sample-input.txt')
    elif mode == "2":
        run_part_b('./input.txt')