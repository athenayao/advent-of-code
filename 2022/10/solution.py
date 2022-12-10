#! python3
import sys

def run_part_1(filename):
    with open(filename, 'r') as file:
        cycle = 0
        x = 1
        all_lines = file.readlines()
        all_lines.reverse()
        total = 0
        while len(all_lines) > 0:
            cycle += 1
            raw_line = all_lines.pop()
            instruction = raw_line.strip().split()

            if (cycle - 20) % 40 == 0:
                signal = cycle * x
                total += signal

            if instruction[0] == 'noop':
                pass
            elif instruction[0] == 'addx':
                all_lines.append(f'addx-pause {instruction[1]}')
            elif instruction[0] == 'addx-pause':
                x += int(instruction[1])
        print(total)

def run_part_2(filename):
    with open(filename, 'r') as file:
        cycle = 0
        x = 1
        all_lines = file.readlines()
        all_lines.reverse()
        cursor = 0
        screen = []

        while len(all_lines) > 0:
            cycle += 1
            raw_line = all_lines.pop()
            instruction = raw_line.strip().split()

            # calculate x bounds
            if x - 1 <= cursor <= x + 1:
                symbol = '#'
            else:
                symbol = '.'
            screen.append(symbol)

            if instruction[0] == 'noop':
                pass
            elif instruction[0] == 'addx':
                all_lines.append(f'addx-pause {instruction[1]}')
            elif instruction[0] == 'addx-pause':
                x += int(instruction[1])

            cursor += 1

            if cycle % 40 == 0:
                cursor = 0
                print(''.join(screen))
                screen = []

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else None
    if not mode:
        mode == "ax"

    if mode == "ax":
        run_part_1('./example.txt')
    elif mode == "a":
        run_part_1("./input.txt")
    elif mode == "bx":
        run_part_2('./example.txt')
    elif mode == "b":
        run_part_2('./input.txt')