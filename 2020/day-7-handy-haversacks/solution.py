import re
import collections

CONTAIN_RE = r'(?P<container>.+) bags? contain (?P<contents>.+)'
CONTENTS_RE = r'(?P<count>\d+) (?P<color>.+?) bags?'

# def parse_rules(rules):
#     container_dict = {}
#     contents_dict = collections.defaultdict(list)

#     for rule in rules:
#         match = re.match(CONTAIN_RE, rule)
#         all_contents = re.findall(CONTENTS_RE, match['contents'])
#         container_dict[match['container']] = all_contents
#         for (count, color) in all_contents:
#             contents_dict[color].append(match['container'])
#     return contents_dict

# def find_options(rules, initial_color):
#     seen = set()
#     queue = rules[initial_color]

#     while len(queue) > 0:
#         current_color = queue.pop()
#         if current_color in seen:
#             continue
#         queue.extend(rules[current_color])
#         seen.add(current_color)
#     return seen

# def run_find_container(lines):
#     rules = parse_rules(lines)
#     options = find_options(rules, 'shiny gold')
#     print(len(options))

def parse_rules(rules):
    container_dict = collections.defaultdict(list)

    for rule in rules:
        match = re.match(CONTAIN_RE, rule)
        all_contents = re.findall(CONTENTS_RE, match['contents'])
        for (count, color) in all_contents:
            for i in range(0, int(count)):
                container_dict[match['container']].append(color)
    return container_dict

def find_contained(rules, search_color):
    if len(rules[search_color]) == 0:
        return []
    
    results = []
    for rule in rules[search_color]:
        results.append(rule)
        results.extend(find_contained(rules, rule))
    return results

def run(lines):
    rules = parse_rules(lines)
    results = find_contained(rules, 'shiny gold')
    print(len(results))
    
if __name__ == '__main__':
    is_example = False
    with open('./input-example.txt' if is_example else './input.txt', 'r') as f:
        run(f.read().splitlines())