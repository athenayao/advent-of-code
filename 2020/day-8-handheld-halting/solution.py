# operation (acc, jmp, or nop)
# argument (a signed number like +4 or -20).

def run_program(program_lines):
    accumulator = 0
    seen_lines = {}
    line_index = 0

    while True:
        if line_index > len(program_lines) - 1:
            break
        (op, arg) = program_lines[line_index]
        if seen_lines.get(line_index, None) is not None:
            return (False, accumulator)

        seen_lines[line_index] = True
        if op == 'nop':
            line_index += 1
        elif op == 'acc':
            accumulator += int(arg)
            line_index += 1
        elif op == 'jmp':
            line_index += int(arg)
    return (True, accumulator)
        
def run(lines):
    for line_index in range(0, len(lines)):
        program_lines = [line.split() for line in lines]
        line = program_lines[line_index]
        op = line[0]
        if op == 'acc':
            continue
        elif op == 'jmp':
            line[0] = 'nop'
        elif op == 'nop':
            line[0] = 'jmp'
        (terminated, accumulator) = run_program(program_lines)
        if terminated:
            print(accumulator)
            break

if __name__ == '__main__':
    is_example = False
    with open('./input-example.txt' if is_example else './input.txt', 'r') as f:
        run(f.read().splitlines())