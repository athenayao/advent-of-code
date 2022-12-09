import os

DIGITS = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

class ParsedType(object):
    ADDITION = 0
    MULTIPLICATION = 1
    NUMBER = 2
    OPEN_PAREN = 3
    CLOSE_PAREN = 4

class Parsed(object):
    t = None
    value = None

    def __init__(self, t, value=None):
        self.t = t
        self.value = value

    def __repr__(self):
        if self.t == ParsedType.ADDITION:
            return '+'
        elif self.t == ParsedType.MULTIPLICATION:
            return '*'
        elif self.t == ParsedType.OPEN_PAREN:
            return '('
        elif self.t == ParsedType.CLOSE_PAREN:
            return ')'
        else:
            return str(self.value)


def parse(text):
    index = 0
    tmp_number = []
    parsed = []

    while True:
        while text[index] in DIGITS:
            tmp_number.append(text[index])
            index += 1
            if index > len(text) - 1:
                break

        if len(tmp_number) > 0:
            parsed.append(Parsed(t=ParsedType.NUMBER, value=int("".join(tmp_number))))
            tmp_number = []

            if index > len(text) - 1:
                break
            continue
        
        char = text[index]

        if char == ' ':
            pass
        elif char == '+':
            parsed.append(Parsed(t=ParsedType.ADDITION))
        elif char == '*':
            parsed.append(Parsed(t=ParsedType.MULTIPLICATION))
        elif char == '(':
            parsed.append(Parsed(t=ParsedType.OPEN_PAREN))
        elif char == ')':
            parsed.append(Parsed(t=ParsedType.CLOSE_PAREN))

        index += 1
        if index > len(text) - 1:
            break
    return parsed

def process(parsed):
    current_value = 0
    current_operation = None

    if len(parsed) == 0:
        return 0

    while len(parsed) > 0:
        item = parsed.pop()
        if item.t == ParsedType.NUMBER:
            if current_operation is None:
                current_value = item.value
            elif current_operation is ParsedType.ADDITION:
                current_value = current_value + item.value
                current_operation = None
            elif current_operation is ParsedType.MULTIPLICATION:
                current_value = current_value * item.value
                current_operation = None
        elif item.t == ParsedType.ADDITION or item.t == ParsedType.MULTIPLICATION:
            current_operation = item.t
        elif item.t == ParsedType.OPEN_PAREN:
            process(parsed)
        elif item.t == ParsedType.CLOSE_PAREN:
            parsed.append(Parsed(t=ParsedType.NUMBER, value=current_value))
            return
    return current_value


def run(lines):
    total = 0
    for line in lines:
        parsed = parse(line)
        parsed.reverse()
        total += process(parsed)
    return total

if __name__ == '__main__':
    is_example = False
    script_dir = os.path.dirname(__file__)
    filename = 'input-example.txt' if is_example else 'input.txt'
    with open(os.path.join(script_dir, filename), 'r') as f:
        answer = run(f.read().splitlines())
        print("### ANSWER ### ")
        print(answer)
        # expect: 26, 437, 12240, 13632
