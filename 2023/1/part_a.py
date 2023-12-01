import os

def is_digit(char):
    return char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' or char == '7' or char == '8' or char == '9'

def run(lines):
    total = 0
    for line in lines:
        subtotal = 0
        for char in line:
            if is_digit(char):
                subtotal += 10 * int(char)
                break

        for char in reversed(line):
            if is_digit(char):
                subtotal += int(char)
                break
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
