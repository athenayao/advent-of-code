import re

INSTRUCTIONS_RE = r'([A-Z])(\d+)'

def calculate_position(direction, value):
    if direction == 'W':
        return ('x', -1 * value)
    elif direction == 'E':
        return ('x', value)
    elif direction == 'N':
        return ('y', -1 * value)
    elif direction == 'S':
        return ('y', value)
    
degrees = {
    'N': 0,
    'E': 90,
    'S': 180,
    'W': 270,
}

directions = {
    0: 'N',
    90: 'E',
    180: 'S',
    270: 'W',
}

def calculate_degrees(degree, direction, value):
    if direction == 'L':
        new_degree = -1 * value + degree
    elif direction == 'R':
        new_degree = value + degree
    normalized = (360 + new_degree if new_degree < 0 else new_degree) % 360
    return normalized

def run(lines):
    degree = degrees['E']

    position = {
        'x': 0,
        'y': 0,
    }

    for line in lines:
        match = re.match(INSTRUCTIONS_RE, line)
        action = match[1]
        value = int(match[2])

        if action == 'F':
            (axis, delta) = calculate_position(directions[degree], value)
            position[axis] += delta
        elif action == 'N' or action == 'S' or action == 'E' or action == 'W':
            (axis, delta) = calculate_position(action, value)
            position[axis] += delta
        elif action == 'L' or action == 'R':
            degree = calculate_degrees(degree, action, value)
    return abs(position['x']) + abs(position['y'])

if __name__ == '__main__':
    is_example = False
    with open('./input-example.txt' if is_example else './input.txt', 'r') as f:
        answer = run(f.read().splitlines())
        print("### ANSWER ### ")
        print(answer)
