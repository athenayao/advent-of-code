#!/usr/bin/python3
import json
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

    def __repr__(self):
        if self.category is not None:
            return f'{self.category}{self.condition}{self.condition_value} -> {self.to}'
        return f'* -> {self.to}'

def parse_workflow(line):
    label, rules_raw = line.split('{')
    rules_raw = rules_raw[0:-1]
    rules = []
    for raw in rules_raw.split(","):
        rules.append(Rule.parse(raw))
    return (label, rules)


global_total = 0

def run_workflow(workflows, workflow, chunk, depth=0):
    global global_total
    if workflow == 'R':
        return
    if workflow == 'A':
        result = 1
        for v in chunk.values():
            result *=  (v[1] - v[0] + 1)
        # print('ACCEPTED', chunk)
        global_total += result
        return
    # print()
    # print(" " * depth * 4, "|", "-" * depth, "Running workflow", workflow, workflows[workflow])
    # print(" " * (depth * 4  + 2), chunk)

    for rule in workflows[workflow]:
        if rule.category is None:
            run_workflow(workflows, rule.to, chunk, depth + 1)
        else:
            satisfies_chunk = dict(chunk)
            leftover_chunk = dict(chunk)

            if rule.condition == '>':
                satisfies_chunk[rule.category] = (
                    rule.condition_value + 1,
                    satisfies_chunk[rule.category][1]
                )
                leftover_chunk[rule.category] = (
                    leftover_chunk[rule.category][0],
                    rule.condition_value
                )
            elif rule.condition == '<':
                satisfies_chunk[rule.category] = (
                    satisfies_chunk[rule.category][0],
                    rule.condition_value - 1
                )
                leftover_chunk[rule.category] = (
                    rule.condition_value,
                    leftover_chunk[rule.category][1],
                )

            print(rule)
            print(satisfies_chunk)
            print(leftover_chunk)
            run_workflow(workflows, rule.to, satisfies_chunk, depth + 1)
            chunk = leftover_chunk


def run(lines):
    workflows = {}
    parsing_workflows = True

    for line in lines:
        if line == '':
            break
        
        label, rules = parse_workflow(line)
        workflows[label] = rules

    
    part_chunks = {
        'x': (1, 4000),
        'm': (1, 4000),
        'a': (1, 4000),
        's': (1, 4000),
    }
    run_workflow(workflows, 'in', part_chunks)
    # min 1, max 4000
    # in{s<1351:px,qqz}
    # so we know 0:1350 -> px, 1351:4k -> qqz
    
    # px{a<2006:qkq,m>2090:A,rfg}
    # x: 0:1350 / a: 0:2005 -> qkq
    # x: 0:1350 / a: 2006:4000 / m:
    return global_total


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