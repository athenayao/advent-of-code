import re

REQUIRED_ATTRIBUTES = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

def is_valid_passport(passport):
    raw_attributes = []
    for line in passport:
        raw_attributes.extend(line.split())

    existing = set()
    for attribute in raw_attributes:
        [key, value] = attribute.split(":")

        if key == 'cid':
            continue
        elif key == 'byr':
            parsed_value = int(value)
            if parsed_value < 1920 or parsed_value > 2002:
                continue
        elif key == 'iyr':
            parsed_value = int(value)
            if parsed_value < 2010 or parsed_value > 2020:
                continue
        elif key == 'eyr':
            parsed_value = int(value)
            if parsed_value < 2020 or parsed_value > 2030:
                continue
        elif key == 'hgt':
            match = re.match("(\d+)(in|cm)", value)
            if match is None:
                continue
            number = int(match[1])
            unit = match[2]
            if unit == 'in':
                if number < 59 or number > 76:
                    continue
            elif unit == 'cm':
                if number < 150 or number > 193:
                    continue
            else:
                continue
        elif key == 'hcl':
            match = re.match('^#(?:[0-9a-f]){6}$', value)
            if match is None:
                continue
        elif key == 'ecl':
            valid_eye_colors = set('amb blu brn gry grn hzl oth'.split())
            if value not in valid_eye_colors:
                continue
        elif key == 'pid':
            match = re.match('^(?:[0-9]){9}$', value)
            if match is None:
                continue
        existing.add(key)
    condition_3 = len(existing) == 7
    
    return condition_3
        
        
def run(lines):
    # collect passport
    passport = []
    num_valid = 0
    for line in lines:
        if line == '':
            if is_valid_passport(passport):
                num_valid += 1
            passport = []
        else:
            passport.append(line)
    if is_valid_passport(passport):
        num_valid += 1
    print(num_valid)
        

if __name__ == '__main__':
    is_example = False
    with open('./input-example.txt' if is_example else './input.txt', 'r') as f:
        run(f.read().splitlines())