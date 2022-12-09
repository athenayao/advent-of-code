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
    

def get_valid_fields(value, fields):
    valid_for = set()
    for field in fields:
        for r in field['ranges']:
            if r[0] <= value <= r[1]:
                valid_for.add(field['name'])
    if len(valid_for) == 0:
        return None
    return valid_for

def get_possible_fields(ticket, fields):
    all_valid = []
    for value in ticket:
        valid_fields = get_valid_fields(value, fields)
        if valid_fields is None:
            return None
        all_valid.append(valid_fields)
    return all_valid
        
        
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
    your_ticket = parse_tickets(groups[1])
    nearby_tickets = parse_tickets(groups[2])

    all_possible_fields = []
    for ticket in nearby_tickets +  your_ticket:
        possible_fields = get_possible_fields(ticket, fields)
        if not possible_fields:
            continue
        all_possible_fields.append(possible_fields)

    # narrow down by logic to common fields across rows
    common_across_rows = []
    for ticket_value_index in range(0, len(all_possible_fields[0])):
        common = all_possible_fields[0][ticket_value_index]
        for row in range(1, len(all_possible_fields)):
            common = common.intersection(all_possible_fields[row][ticket_value_index])
        common_across_rows.append(common)
    

    # narrow down logic to what has only one possibility
    final_mapping = {}
    while len(final_mapping) < len(common_across_rows):
        finalized = set()
        for index, field_names in enumerate(common_across_rows):
            if len(field_names) == 1:
                finalized.update(field_names)

        for i, f in enumerate(common_across_rows):
            if len(f) == 1:
                final_mapping[f.pop()] = i
            common_across_rows[i] = f.difference(finalized)
    
    final_answer = 1
    for field_name, field_index in final_mapping.items():
        if field_name.startswith('departure'):
            final_answer *= your_ticket[0][field_index]
    return final_answer


if __name__ == '__main__':
    is_example = False
    script_dir = os.path.dirname(__file__)
    filename = 'input-example.txt' if is_example else 'input.txt'
    with open(os.path.join(script_dir, filename), 'r') as f:
        answer = run(f.read().splitlines())
        print("### ANSWER ### ")
        print(answer)
