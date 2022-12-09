def find_invalid_number(lines, preamble):
    inputs = []
    window = set()
    for index, current_number in enumerate(lines):
        is_valid = False
        inputs.append(current_number)
        if index >= preamble:
            window = set(inputs[len(inputs) - (preamble + 1):-1])
            for window_number in window:
                delta = current_number - window_number
                if delta in window and delta != window_number:
                    is_valid = True
                    break
            if not is_valid:
                return current_number

def run(lines, preamble):
    lines = [int(line) for line in lines]
    invalid_number = find_invalid_number(lines, preamble)
    for index, line in enumerate(lines):
        current_sum = 0
        current_inputs = []
        for i in range(0, len(lines) - index - 1):
            current_sum += lines[index + i]
            if current_sum > invalid_number:
                break
            current_inputs.append(lines[index+i])
            if current_sum == invalid_number:
                print(min(current_inputs) + max(current_inputs))
                return
            

if __name__ == '__main__':
    is_example = False
    with open('./input-example.txt' if is_example else './input.txt', 'r') as f:
        run(f.read().splitlines(), 5 if is_example else 25)