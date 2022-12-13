#! python3
import sys

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
        
        else:
            if left_is_int:
                left_item = [left_item]

            if right_is_int:
                right_item = [right_item]
            
            return compare_lists(left_item, right_item)
        
    return True

def run_part_1(filename):
    with open(filename, 'r') as file:
        left = None
        right = None

        pair_index = 0
        ordered_pairs = []
        for raw_line in file.readlines():
            line = raw_line.strip()
            if not line:
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
        print(sum(ordered_pairs))



def run_part_2(filename):
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
        run_part_1('./example.txt')
    elif mode == "a":
        run_part_1("./input.txt")
    elif mode == "bx":
        run_part_2('./example.txt')
    elif mode == "b":
        run_part_2('./input.txt')