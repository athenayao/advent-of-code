import os

DIGITS = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

class TermType(object):
    ADDITION = 0
    MULTIPLICATION = 1
    NUMBER = 2
    # errr
    EXPRESSION = 3

ORDER = {
    TermType.ADDITION: 1,
    TermType.MULTIPLICATION: 2,
}

class Expression(object):
    def __init__(self):
        self.terms = []
        self. t = TermType.EXPRESSION

    def add_term(self, term):
        self.terms.append(term)
    
    def pop(self, index=None):
        return self.terms.pop(index)

    def __repr__(self):
        return '(%s)' % " ".join([str(term) for term in self.terms])

    def __len__(self):
        return len(self.terms)
    
class Term(object):
    def __init__(self, t, value=None):
        self.t = t
        self.value = value

    def __repr__(self):
        if self.t == TermType.ADDITION:
            return '+'
        elif self.t == TermType.MULTIPLICATION:
            return '*'
        else:
            return str(self.value)


def parse(text):
    tmp_number = []
    parsed = Expression()
    
    operators = []
    terms = []

    while True:
        while text[0] in DIGITS:
            tmp_number.append(text.pop(0))
            if len(text) == 0:
                break

        if len(tmp_number) > 0:
            parsed.add_term(Term(t=TermType.NUMBER, value=int("".join(tmp_number))))
            tmp_number = []

            if len(text) == 0:
                break
            continue
        
        char = text.pop(0)

        if char == ' ':
            pass
        elif char == '+' or char == '*':
            if char == '+':
                op = Term(t=TermType.ADDITION)
            elif char == '*':
                op = Term(t=TermType.MULTIPLICATION)

            while len(operators) > 0 and ORDER[op.t] >= ORDER[operators[-1].t]:
                parsed.add_term(operators.pop())
            operators.append(op)
        elif char == '(':
            parsed.add_term(parse(text))
        elif char == ')':
            break

        if len(text) == 0:
            break
    while len(operators) > 0:
        parsed.add_term(operators.pop())
    return parsed

def process(parsed):
    current_value = 0
    current_operation = None
    number_stack = []

    if len(parsed) == 0:
        return 0
    
    while len(parsed) > 0:
        item = parsed.pop(0)
        if item.t == TermType.NUMBER:
            number_stack.append(item.value)
        elif item.t == TermType.ADDITION:
            number_stack.append(number_stack.pop() + number_stack.pop())
        elif item.t == TermType.MULTIPLICATION:
            number_stack.append(number_stack.pop() * number_stack.pop())
        elif item.t == TermType.EXPRESSION:
            number_stack.append(process(item))
    return number_stack.pop()
            

def run(lines):
    total = 0
    for line in lines:
        parsed = parse(list(line))
        expression_result = process(parsed)
        print(expression_result)
        total += expression_result
    return total

if __name__ == '__main__':
    is_example = False
    script_dir = os.path.dirname(__file__)
    filename = 'input-example.txt' if is_example else 'input.txt'
    with open(os.path.join(script_dir, filename), 'r') as f:
        answer = run(f.read().splitlines())
        print("### ANSWER ### ")
        print(answer)
        # expect: 231, 51, 46, 1445, 669060, 23340

