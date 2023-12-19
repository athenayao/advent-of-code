#!/usr/bin/python3
import argparse
import sys
import os
import re

RULE_REGEX = re.compile('(?P<category>[xmas])(?P<condition>[><])(?P<condition_value>\d+):(?P<to>.+)')
class Rule:
    def __init__(self, to, category=None, condition=None, condition_value=None):
        self.category = category
        self.condition = condition
        self.condition_value = int(condition_value) if condition_value is not None else None
        self.to = to
    
    @staticmethod
    def parse(raw):
        match = RULE_REGEX.match(raw)
        if match:
            return Rule(
                to=match.group('to'),
                category=match.group('category'),
                condition=match.group('condition'),
                condition_value=match.group('condition_value')
            )
        else:
            return Rule(to=raw)

    def get_next(self, part):
        if not self.condition:
            return self.to
        
        if self.condition == '>' and part[self.category] > self.condition_value:
            return self.to
        if self.condition == '<' and part[self.category] < self.condition_value:
            return self.to

        return None

def parse_workflow(line):
    label, rules_raw = line.split('{')
    rules_raw = rules_raw[0:-1]
    rules = []
    for raw in rules_raw.split(","):
        rules.append(Rule.parse(raw))
    return (label, rules)


PART_REGEX = re.compile('{x=(?P<x>(\d+)),m=(?P<m>(\d+)),a=(?P<a>(\d+)),s=(?P<s>(\d+))}')
def parse_part(raw):
    match = PART_REGEX.match(raw)
    return {'x': int(match.group('x')), 'm': int(match.group('m')), 'a': int(match.group('a')), 's': int(match.group('s'))}

def run_workflow(workflows, part, workflow):
    for rule in workflows[workflow]:
        result = rule.get_next(part)
        if result == 'A':
            return True
        
        if result == 'R':
            return False
        
        if result:
            return run_workflow(workflows, part, result)



def run(lines):
    workflows = {}
    parsing_workflows = True

    total = 0
    for line in lines:
        if line == '':
            parsing_workflows = False
            continue

        if parsing_workflows:
            label, rules = parse_workflow(line)
            workflows[label] = rules

        else:
            part = parse_part(line)
            accepted = run_workflow(workflows, part, 'in')
            if accepted:
                total += sum(part.values())

    return total
            





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