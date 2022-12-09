import re

INSTRUCTIONS_RE = r'([A-Z])(\d+)'

def calculate_waypoint_offset(direction, value):
    if direction == 'W':
        return ('x', -1 * value)
    elif direction == 'E':
        return ('x', value)
    elif direction == 'N':
        return ('y', -1 * value)
    elif direction == 'S':
        return ('y', value)


directions = {
    0: 'N',
    90: 'E',
    180: 'S',
    270: 'W',
}

def rotate_waypoint(waypoint_offset, action, value):
    if action == 'L':
        delta = -1 * value
    elif action == 'R':
        delta = value
    normalized = (360 + delta if delta < 0 else delta) % 360

    if normalized == 0:
        return waypoint_offset
    if normalized == 90:
        return {
            'x': -1 * waypoint_offset['y'],
            'y': waypoint_offset['x'],
        }
    elif normalized == 180:
        return {
            'x': -1 * waypoint_offset['x'],
            'y': -1 * waypoint_offset['y'],
        }
    elif normalized == 270:
        return {
            'x': waypoint_offset['y'],
            'y': -1 * waypoint_offset['x'],
        }

def run(lines):
    waypoint_offset = {
        'x': 10,
        'y': -1,
    }

    ship_position = {
        'x': 0,
        'y': 0,
    }

    for line in lines:
        match = re.match(INSTRUCTIONS_RE, line)
        action = match[1]
        value = int(match[2])

        if action == 'F':
            ship_position['x'] += waypoint_offset['x'] * value
            ship_position['y'] += waypoint_offset['y'] * value
        elif action == 'N' or action == 'S' or action == 'E' or action == 'W':
            (axis, delta) = calculate_waypoint_offset(action, value)
            waypoint_offset[axis] += delta
        elif action == 'L' or action == 'R':
            waypoint_offset = rotate_waypoint(waypoint_offset, action, value)
    return abs(ship_position['x']) + abs(ship_position['y'])


if __name__ == '__main__':
    is_example = False
    with open('./input-example.txt' if is_example else './input.txt', 'r') as f:
        answer = run(f.read().splitlines())
        print("### ANSWER ### ")
        print(answer)
