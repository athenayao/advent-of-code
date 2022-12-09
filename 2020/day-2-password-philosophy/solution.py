def parse_sled(line):
    [range_allowed, letter, password] = line.split(" ")
    [min_range, max_range] = range_allowed.split('-')
    return {
        'min': int(min_range),
        'max': int(max_range),
        'letter': letter.rstrip(':'),
        'password': password
    }

def is_valid_sled(line):
    parsed = parse(line)
    num_matching_chars = 0
    for char in parsed['password']:
        if char == parsed['letter']:
            num_matching_chars += 1
    return parsed['min'] <= num_matching_chars <= parsed['max']

def parse(line):
    [range_allowed, letter, password] = line.split(" ")
    [first, second] = range_allowed.split('-')
    return {
        'first_index': int(first),
        'second_index': int(second),
        'letter': letter.rstrip(':'),
        'password': password
    }

def is_valid(line):
    parsed = parse(line)
    password = parsed['password']
    first_matched = password[parsed['first_index'] - 1] == parsed['letter']
    second_matched = password[parsed['second_index'] - 1] == parsed['letter']
    return first_matched ^ second_matched
    

def run(lines):
    num_valid = 0
    for line in lines:
        if is_valid(line):
            num_valid += 1
    print(num_valid)


if __name__ == '__main__':
    is_example = True
    with open('./input-example.txt' if is_example else './input.txt', 'r') as f:
        run(f.readlines())

    