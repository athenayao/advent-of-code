#! python3
import sys
import re

def run_part_1(filename):
    with open(filename, 'r') as file:
        raw_columns = []
        raw_lines = (line[:-1] for line in file.readlines())
        for line in raw_lines:
            if not line:
                break        
            raw_columns.append(list(line))
        num_columns = len(''.join(raw_columns.pop()).split())
        num_rows = len(raw_columns)

        columns = []
        for column_index in range(0, num_columns):
            columns.append([])
            for row in range(num_rows, 0, -1):
                column = columns[column_index]
                char = raw_columns[row-1][column_index * 4 + 1]
                if char != ' ':
                    column.append(char)

        for line in raw_lines:
            line = line.strip()
            match = re.match(r'move (\d+) from (\d+) to (\d+)', line)

            num_move = int(match[1])
            from_column = int(match[2]) - 1 
            to_column = int(match[3]) - 1

            for _ in range(0, num_move):
                value = columns[from_column].pop()
                columns[to_column].append(value)

        print(''.join([column[-1] for column in columns]))

def run_part_2(filename):
    with open(filename, 'r') as file:
        raw_columns = []
        raw_lines = (line[:-1] for line in file.readlines())
        for line in raw_lines:
            if not line:
                break        
            raw_columns.append(list(line))
        num_columns = len(''.join(raw_columns.pop()).split())
        num_rows = len(raw_columns)

        columns = []
        for column_index in range(0, num_columns):
            columns.append([])
            for row in range(num_rows, 0, -1):
                column = columns[column_index]
                char = raw_columns[row-1][column_index * 4 + 1]
                if char != ' ':
                    column.append(char)

        for line in raw_lines:
            line = line.strip()
            match = re.match(r'move (\d+) from (\d+) to (\d+)', line)

            num_move = int(match[1])
            from_column = int(match[2]) - 1 
            to_column = int(match[3]) - 1

             # maintain the order
            split_at = len(columns[from_column]) - num_move 
            stack = columns[from_column][split_at:]
            columns[from_column] = columns[from_column][0:split_at ]
            columns[to_column].extend(stack)

        print(''.join([column[-1] for column in columns]))


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else None
    if not mode:
        mode == "ax"

    if mode == "ax":
        run_part_1('./sample-input.txt')
    elif mode == "a":
        run_part_1("./input.txt")
    elif mode == "bx":
        run_part_2('./sample-input.txt')
    elif mode == "b":
        run_part_2('./input.txt')