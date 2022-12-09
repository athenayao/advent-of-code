import functools
import collections

def calc_question_count(current_group, current_group_count):
    question_count = 0
    for count in current_group.values():
        if count == current_group_count:
            question_count += 1
    return question_count

def run(lines):
    groups = []
    current_group = collections.defaultdict(int)
    current_group_count = 0
    actual_sum = 0

    for line in lines:
        if line == '':
            actual_sum += calc_question_count(current_group, current_group_count)
            current_group = collections.defaultdict(int)
            current_group_count = 0 
        else:
            for char in line:
                current_group[char] += 1
            current_group_count += 1
    actual_sum += calc_question_count(current_group, current_group_count)
    print(actual_sum)

if __name__ == '__main__':
    is_example = False
    with open('./input-example.txt' if is_example else './input.txt', 'r') as f:
        run(f.read().splitlines())