#! /Users/athena/.nix-profile/bin/python

def run(filename):
    with open(filename, 'r') as file:
        current_max = 0
        elf = []
        for raw_line in file.readlines():
            line = raw_line.strip()
            if not len(line):
                total = sum(elf)
                current_max = max(current_max, sum(elf))
                elf = []
            else:
                elf.append(int(line))
        current_max = max(current_max, sum(elf))
    print(current_max)

def run_part_2(filename):
    with open(filename, 'r') as file:
        totals = []
        elf = []
        for raw_line in file.readlines():
            line = raw_line.strip()
            if not len(line):
                totals.append(sum(elf))
                elf = []
            else:
                elf.append(int(line))
        totals.append(sum(elf))
    totals.sort(reverse=True)
    print(sum(totals[0:3]))


if __name__ == '__main__':
    # run_part_2('./sample-input.txt')
    run_part_2('./input.txt')