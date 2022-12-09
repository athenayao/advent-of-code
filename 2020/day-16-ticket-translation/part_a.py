import os
import re

def parse_ranges(ranges):
    parsed = []
    for r in ranges.split(" or "):
        start, end = r.strip().split("-")
        parsed.append((int(start), int(end)))
    return parsed

def parse_fields(input_lines):
    fields = []
    for line in input_lines:
        field_name, ranges = line.split(":")
        fields.append({
            'name': field_name,
            'ranges': parse_ranges(ranges)
        })
    return fields

def parse_ticket(input_line):
    return [int(v) for v in input_line.split(",")]

def parse_tickets(input_lines):
    return [parse_ticket(line) for line in input_lines[1:]]
    

def find_valid_value(value, fields):
    for field in fields:
        for r in field['ranges']:
            if r[0] <= value <= r[1]:
                return True
    return False

def find_invalid_values(ticket, fields):
    invalid_values = []
    for value in ticket:
        if not find_valid_value(value, fields):
            invalid_values.append(value)
    return invalid_values
        
        
def run(lines):
    groups = []
    group = []
    for line in lines:
        if line == '':
            groups.append(group)
            group = []
        else:
            group.append(line)
    groups.append(group)

    fields = parse_fields(groups[0])
    nearby_tickets = parse_tickets(groups[2])

    error_rate = 0
    for ticket in nearby_tickets:
        error_rate += sum(find_invalid_values(ticket, fields))
    return error_rate


if __name__ == '__main__':
    is_example = False
    script_dir = os.path.dirname(__file__)
    filename = 'input-example.txt' if is_example else 'input.txt'
    with open(os.path.join(script_dir, filename), 'r') as f:
        answer = run(f.read().splitlines())
        print("### ANSWER ### ")
        print(answer)
