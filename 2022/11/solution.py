#! python3
import sys

def get_last_int(string):
    return int(string.split()[-1])

class Monkey:
    def __init__(self, id, items, operation, divisible_by, if_true, if_false):
        self.id = id
        self.items = items
        self.operation = operation
        self.divisible_by = divisible_by
        self.if_true = if_true
        self.if_false = if_false
        self.inspected = 0

    def __repr__(self):
        return f'Monkey {self.id} {self.items}'

    @classmethod
    def parse(cls, lines):
        items = [int(x) for x in lines[1].split(':')[1].split(',')]
        return cls(
            id=get_last_int(lines[0][:-1]),
            items=items,
            operation=lines[2].split("=")[1],
            divisible_by=get_last_int(lines[3]),
            if_true=get_last_int(lines[4]),
            if_false=get_last_int(lines[5]),
        )

def run_part_1(filename):
    with open(filename, 'r') as file:
        all_lines = [line.strip() for line in file.readlines()]
    
        monkeys = []
        for i in range(0, len(all_lines), 7):
            monkey = Monkey.parse(all_lines[i:i+7])
            monkeys.append(monkey)
        
        for i in range(20):
            for monkey in monkeys:
                monkey.inspected += len(monkey.items)
                for item in monkey.items:
                    worry_level = item
                    worry_level = eval(monkey.operation, {}, {'old': worry_level})
                    worry_level = worry_level // 3

                    if worry_level % monkey.divisible_by == 0:
                        monkeys[monkey.if_true].items.append(worry_level)
                    else:
                        monkeys[monkey.if_false].items.append(worry_level)
                print(monkeys)
                monkey.items = []
        monkey_business = [monkey.inspected for monkey in monkeys]
        monkey_business = sorted(monkey_business, reverse=True)
        print(monkey_business, monkey_business[0] * monkey_business[1])




def run_part_2(filename):
    with open(filename, 'r') as file:
        all_lines = [line.strip() for line in file.readlines()]
    
        common = 1
        monkeys = []
        for i in range(0, len(all_lines), 7):
            monkey = Monkey.parse(all_lines[i:i+7])
            common *= monkey.divisible_by
            monkeys.append(monkey)
        print(common)
        
        for i in range(10_000):
            for monkey in monkeys:
                monkey.inspected += len(monkey.items)
                for item in monkey.items:
                    worry_level = item
                    worry_level = eval(monkey.operation, {}, {'old': worry_level})
                    worry_level = worry_level % common

                    if worry_level % monkey.divisible_by == 0:
                        monkeys[monkey.if_true].items.append(worry_level)
                    else:
                        monkeys[monkey.if_false].items.append(worry_level)
                monkey.items = []
            if i + 1 in (1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10_000):
                print(i + 1, [monkey.inspected for monkey in monkeys])

        monkey_business = [monkey.inspected for monkey in monkeys]
        monkey_business = sorted(monkey_business, reverse=True)
        print(monkey_business, monkey_business[0] * monkey_business[1])

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