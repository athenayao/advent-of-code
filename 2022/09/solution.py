#! python3
import sys
from collections import namedtuple


Point = namedtuple('Point', 'row, col, value')

def move_point(point, direction):
    if direction == 'U':
        return Point(point.row - 1, point.col, point.value)
    elif direction == 'D':
        return Point(point.row + 1, point.col, point.value)
    elif direction == 'L':
        return Point(point.row, point.col - 1, point.value)
    elif direction == 'R':
        return Point(point.row, point.col + 1, point.value)

def is_touching(point_1, point_2):
    return abs(point_1.row - point_2.row) <= 1 and abs(point_1.col - point_2.col) <= 1

def two_away(point_1, point_2):
    if point_1.row == point_2.row:
        distance = point_1.col - point_2.col
        if distance == -2:
            return 'L'
        elif distance == 2:
            return 'R'
    
    if point_1.col == point_2.col:
        distance = point_1.row - point_2.row
        if distance == -2:
            return 'U'
        elif distance == 2:
            return 'D'

    return None


def run_part_1(filename):
    with open(filename, 'r') as file:
        head = Point(0, 0, 'H')
        tail = Point(0, 0, 'T')
        seen = set()
        for raw_line in file.readlines():
            (direction, steps) = raw_line.strip().split()
            steps = int(steps)

            # move head
            for _ in range(0, steps):
                seen.add(tail)
                head = move_point(head, direction)
            
                if is_touching(head, tail):
                    continue

                calc_two_away = two_away(head, tail)
                if calc_two_away:
                    tail = move_point(tail, calc_two_away)
                    continue
                
                # going to assume that this is just an else...
                if head.row - tail.row > 0:
                    new_row = tail.row + 1
                else:
                    new_row = tail.row - 1
                
                if head.col - tail.col > 0:
                    new_col = tail.col + 1
                else:
                    new_col = tail.col - 1
                tail = Point(new_row, new_col)

        seen.add(tail)
        print(len(seen))
            # then calculate where to move tail
            


def run_part_2(filename):
    with open(filename, 'r') as file:
        points = []
        for i in range(0, 10):
            if i == 0:
                points.append(Point(0, 0, 'H'))
            else:
                points.append(Point(0, 0, str(i)))

        min_col = 0
        max_col = 0
        min_row = 0
        max_row = 0

        seen = set()
        for raw_line in file.readlines():
            (direction, steps) = raw_line.strip().split()
            steps = int(steps)

            # move head
            for _ in range(0, steps):
                print_grid(points, f"{direction} - {steps}")
                # min_col = min([p.col for p in points] + [min_col])
                # max_col = max([p.col for p in points] + [max_col])
                # min_row = min([p.row for p in points] + [min_row])
                # max_row = max([p.row for p in points] + [max_row])

                seen.add(points[-1])

                points[0] = move_point(points[0], direction)

                for pi, point in enumerate(points[1:], 1):
                    leader = points[pi - 1]
                    follower = points[pi]
                
                    if is_touching(leader, follower):
                        continue

                    calc_two_away = two_away(leader, follower)
                    if calc_two_away:
                        points[pi] = move_point(points[pi], calc_two_away)
                        continue
                
                    # going to assume that this is just an else...
                    if leader.row - follower.row > 0:
                        new_row = follower.row + 1
                    else:
                        new_row = follower.row - 1
                    
                    if leader.col - follower.col > 0:
                        new_col = follower.col + 1
                    else:
                        new_col = follower.col - 1
                    points[pi] = Point(new_row, new_col, points[pi].value)

        # min_col = min([p.col for p in points] + [min_col])
        # max_col = max([p.col for p in points] + [max_col])
        # min_row = min([p.row for p in points] + [min_row])
        # max_row = max([p.row for p in points] + [max_row])
        seen.add(points[-1])

        print(min_col, max_col, min_row, max_row)
        print(len(seen))

def print_grid(points, command):
    points_map = {}
    for p in points:
        key = f'{p.col}-{p.row}'
        if key in points_map:
            continue
        points_map[key] = p

    min_col = -5
    max_col = 8
    min_row = -5
    max_row = 3
    
    print()
    print(command)
    for row in range(min_row, max_row + 1):
        line = []
        for col in range(min_col, max_col + 1):
            key = f'{col}-{row}'
            value = points_map.get(key, None)
            if value is None:
                value = '.'
            else:
                value = value.value

            line.append(value)
        print(''.join(line))



if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else None
    if not mode:
        mode == "ax"

    if mode == "ax":
        run_part_1('./sample-input.txt')
    elif mode == "a":
        run_part_1("./input.txt")
    elif mode == "bx":
        run_part_2('./sample-input.txt')
    elif mode == "b":
        run_part_2('./input.txt')

