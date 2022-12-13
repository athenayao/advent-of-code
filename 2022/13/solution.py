#! python3
import sys
import functools

def parse_token(token_array):
    return int(''.join(token_array))

def parse(raw_data, index=0):
    array = []
    token = []

    while True:
        if index > len(raw_data) - 1:
            return array[0]
        char = raw_data[index]

        index += 1
        if char == '[':
            if token:
                array.append(parse_token(token))
                token = []
            stack, index = parse(raw_data, index)
            array.append(stack)
        elif char == ']':
            if token:
                array.append(parse_token(token))
                token = []
            return (array, index)
        elif char == ',':
            if token:
                array.append(parse_token(token))
                token = []

        else:
            token.append(char)


def compare_lists(left, right):
    # import pdb; pdb.set_trace()
    for i in range(max(len(left), len(right))):

        if i > len(left) - 1:
            return True
        elif i > len(right) - 1:
            return False

        left_item = left[i]
        right_item = right[i]
    
        left_is_int = type(left_item) == int
        right_is_int = type(right_item) == int

        if left_is_int and right_is_int:
            if left_item > right_item:
                return False
            elif left_item < right_item:
                return True
        else:
            if left_is_int:
                left_item = [left_item]

            if right_is_int:
                right_item = [right_item]
            
            ret = compare_lists(left_item, right_item)
            if ret is not None:
                return ret
        
    return None

def run_part_1(filename):
    with open(filename, 'r') as file:
        left = None
        right = None

        pair_index = 0
        ordered_pairs = []
        lines = file.readlines()
        for raw_line in lines:
            line = raw_line.strip()
            if not line or line[0] != '[':
                continue
            
            if left is None:
                left = parse(line)
            elif right is None:
                right = parse(line)

            correct = True
            if left is not None and right is not None:
                pair_index += 1
        
                correct = compare_lists(left, right)
        
                if correct:
                    ordered_pairs.append(pair_index)

                left = None
                right = None
        print(sum(ordered_pairs), '=', ordered_pairs)


def cmp_lines(left, right):
    result = compare_lists(left[0], right[0])
    if result is None:
        return 0
    elif result:
        return -1
    else:
        return 1

    
def run_part_2(filename):
    with open(filename, 'r') as file:
        all_lines = file.readlines()
        divider_one = '[[2]]'
        divider_two = '[[6]]'
        all_lines.append(divider_one)
        all_lines.append(divider_two)
        all_lines = [(parse(line.strip()), line.strip()) for line in all_lines if line.strip() != '']

        sorted_list = sorted(all_lines, key=functools.cmp_to_key(cmp_lines))

        total = 1
        for index, (_, raw_line) in enumerate(sorted_list):
            if raw_line == divider_one or raw_line == divider_two:
                total *= index + 1
        print(total)


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