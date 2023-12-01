import os

def is_digit(char):
    return char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' or char == '7' or char == '8' or char == '9'

digit_map = {
    'one':1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

digit_words = digit_map.keys()

def get_digit(line):
    if is_digit(line[0]):
        return int(line[0])
    for word in digit_words:
        if line.startswith(word):
            return digit_map[word]
    return None
    # return line.startswith(digit_words)

def run(lines):
    total = 0
    for line in lines:
        subtotal = 0
        i = 0

        curdigit = 0
        for i in range(0, len(line), 1):
            digit = get_digit(line[i:])
            if digit is not None:
                subtotal += 10 * digit
                curdigit = digit
                break

        for i in range(len(line) - 1, 0, -1):
            digit = get_digit(line[i:])
            if digit is not None:
                subtotal += digit
                curdigit = 0
                break
        subtotal += curdigit
        print(subtotal)
        total += subtotal
    return total


if __name__ == '__main__':
    is_example = False
    script_dir = os.path.dirname(__file__)
    filename = 'input-example.txt' if is_example else 'input.txt'
    with open(os.path.join(script_dir, filename), 'r') as f:
        answer = run(f.read().splitlines())
        print("### ANSWER ### ")
        print(answer)
