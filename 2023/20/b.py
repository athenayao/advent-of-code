#!/usr/bin/python3
import enum
from collections import defaultdict
import argparse
import sys
import os


class ModuleType(enum.Enum):
    FLIP_FLOP = '%'
    CONJUNCTION = '&'
    BROADCASTER = '>'

# lol
class Pulse(enum.Enum):
    HIGH = '-high-'
    LOW = '-low-'

class Module:
    def __init__(self, label, module_type, to):
        self.label = label
        self.type = module_type
        self.to = to

    @staticmethod
    def parse(line):
        from_, to = line.split("->")
        to = [x.strip() for x in to.split(",")]

        from_ = from_.strip()
        module_type = None
        if from_ == 'broadcaster':
            module_type = ModuleType.BROADCASTER
            label = from_
            return Broadcaster(label=from_, module_type=ModuleType.BROADCASTER, to=to)
        else:
            type_character = from_[0]
            label = from_[1:]
            if type_character == '%':
                return FlipFlop(label=label, module_type=ModuleType.FLIP_FLOP, to=to)
            else:
                return Conjunction(label=label, module_type=ModuleType.CONJUNCTION, to=to)

            
    def __repr__(self):
        return f'{self.type.value}{self.label}'


class Broadcaster(Module):
    def __init__(self, label, module_type, to):
        return super().__init__(label, module_type, to)
    
    def get_next(self, pulse, from_input):
        return pulse        


class FlipFlop(Module):
    def __init__(self, label, module_type, to):
        self.on = False
        return super().__init__(label, module_type, to)

    def get_next(self, pulse, from_input):
        if pulse == Pulse.HIGH:
            return None
        if pulse == Pulse.LOW:
            if self.on:
                self.on = False
                return Pulse.LOW
            else:
                self.on = True
                return Pulse.HIGH

class Conjunction(Module):
    def __init__(self, label, module_type, to):
        self.inputs = {}
        return super().__init__(label, module_type, to)

    def add_input(self, label):
        self.inputs[label] = False
    
    def get_next(self, pulse, from_input):
        self.inputs[from_input] = pulse
        return Pulse.LOW if all([x == Pulse.HIGH for x in self.inputs.values()]) else Pulse.HIGH

# detect cycles?
def push_button(modules, expected, seen_counts):
    to_process = [('button', 'broadcaster', Pulse.LOW)]

    counts = defaultdict(int)
    while to_process:
        (from_label, to_label, from_pulse) = to_process.pop(0)
        seen_counts[(from_label, to_label, from_pulse)] += 1
        if to_label == expected and from_pulse == Pulse.LOW:
            return True
        # print(f'{from_label} {from_pulse.value}> {to_label}')
        if to_label not in modules:
            continue
        next_pulse = modules[to_label].get_next(from_pulse, from_label)
        if next_pulse is None:
            continue

        for next_label in modules[to_label].to:
            to_process.append((to_label, next_label, next_pulse))

    return False
        
def run(lines):
    modules = {}

    conj_modules = set()
    for line in lines:
        module = Module.parse(line)
        modules[module.label] = module
        if module.type == ModuleType.CONJUNCTION:
            conj_modules.add(module.label)
    
    for module in modules.values():
        for to in module.to:
            if to in conj_modules:
                modules[to].add_input(module.label)

    seen_counts = defaultdict(int)
    counter = 0
    while True:
        counter += 1
        if push_button(modules, 'rx', seen_counts):
            break
        if counter % 100 == 0:
            import pdb; pdb.set_trace()
    return counter



if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='run.py')
    parser.add_argument('-x', '--example', action='store_true')
    args = parser.parse_args()

    filename = 'input-example.txt' if args.example else 'input.txt'

    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, filename), 'r') as f:
        answer = run(f.read().splitlines())
        print("### ANSWER ### ")
        print(answer)