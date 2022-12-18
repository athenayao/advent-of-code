#! python3
import sys
import re
from collections import namedtuple, defaultdict

Point = namedtuple('Point', 'x, y')
Range = namedtuple('Range', 'start, end')

BEACON = 'B'
SENSOR = 'S'
NOT_PRESENT = '#'

INPUT_REGEX = r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)'


def print_grid(rows):
    for row in range(-10, 30):
        row_value = []
        for col in range(-10, 30):
            row_value.append(rows[row].get(col, '.'))
        print(''.join(row_value))

def get_distance(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def mark_range(rows, sensor, beacon, ROW_NUMBER):
    min_distance = get_distance(sensor, beacon)

    y = ROW_NUMBER
    for x in range(sensor.x - min_distance, sensor.x + min_distance + 1):
        new_point = Point(x, y)
        if get_distance(sensor, new_point) <= min_distance:
            if new_point.x not in rows[new_point.y]:
                rows[new_point.y][new_point.x] = '#'

def run_part_1(filename, is_example=False):
    rows = defaultdict(dict)

    with open(filename, 'r') as file:
        ROW_NUMBER = 10 if is_example else 200_0000

        for raw_line in file.readlines():
            line = raw_line.strip()
            match = re.match(INPUT_REGEX, line)
            sensor = Point(int(match[1]), int(match[2]))
            beacon = Point(int(match[3]), int(match[4]))

            rows[sensor.y][sensor.x] = SENSOR
            rows[beacon.y][beacon.x] = BEACON

            mark_range(rows, sensor, beacon, ROW_NUMBER)

        print_grid(rows)
        
        print(len([x for x in rows[ROW_NUMBER].values() if x == '#']))


def combine_ranges(ranges, max_size):
    sorted_ranges = sorted(ranges, key=lambda x: x[0], reverse=True)

    new_ranges = []
    prev_range = None
    new_range_start = None
    new_range_end = None
    while len(sorted_ranges):
        if not prev_range:
            prev_range = sorted_ranges.pop()

        cur_range = sorted_ranges.pop()
        
        if prev_range.start - 1 <= cur_range.start <= prev_range.end + 1:
            new_range_start = min(prev_range.start, cur_range.start)
            new_range_end = max(prev_range.end, cur_range.end)
            prev_range = Range(new_range_start, new_range_end)
        else:
            new_ranges.append(Range(prev_range.start, prev_range.end))
            prev_range = cur_range
    new_ranges.append(prev_range)

    return [Range(range.start, min(range.end, max_size)) for range in new_ranges]


def run_part_2(filename, is_example=False):
    with open(filename, 'r') as file:
        MAX_SIZE = 20 if is_example else 4_000_000
        ranges = defaultdict(list)

        for raw_line in file.readlines():
            line = raw_line.strip()
            match = re.match(INPUT_REGEX, line)
            sensor = Point(int(match[1]), int(match[2]))
            beacon = Point(int(match[3]), int(match[4]))

            min_distance = get_distance(sensor, beacon)

            # I am tired, this could be one loop
            # range same size
            y = sensor.y
            ranges[y].append(Range(sensor.x - min_distance, sensor.x + min_distance))

            # going up
            for delta_y in range(1, min_distance + 1):
                ranges[sensor.y + delta_y].append(Range(sensor.x - (min_distance - delta_y), sensor.x + (min_distance - delta_y)))
            
            # going down
            for delta_y in range(-1, -1 * min_distance - 1, -1):
                ranges[sensor.y + delta_y].append(Range(sensor.x - (min_distance + delta_y), sensor.x + (min_distance + delta_y)))
            
            ranges[beacon.y].append(Range(beacon.x, beacon.x))

        # combine_ranges([Range(start=15, end=25), Range(start=15, end=17), Range(start=11, end=13), Range(start=3, end=13), Range(start=2, end=2), Range(start=-3, end=3)], 20)
        # the ranges should also take into account the sensor and the beacon
        # combine ranges
        for y in range(0, MAX_SIZE + 1):
            combined = combine_ranges(ranges[y], max_size=MAX_SIZE)
            if len(combined) > 1:
                print((combined[0].end + 1) * 4_000_000 + y)
                break
        


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else None
    if not mode:
        mode == "ax"

    if mode == "ax":
        run_part_1('./example.txt', is_example=True)
    elif mode == "a":
        run_part_1("./input.txt")
    elif mode == "bx":
        run_part_2('./example.txt', is_example=True)
    elif mode == "b":
        run_part_2('./input.txt')