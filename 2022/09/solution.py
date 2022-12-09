#! python3
import sys
from collections import namedtuple


Point = namedtuple('Point', 'row, col')

def move_point(point, direction):
    if direction == 'U':
        return Point(point.row - 1, point.col)
    elif direction == 'D':
        return Point(point.row + 1, point.col)
    elif direction == 'L':
        return Point(point.row, point.col - 1)
    elif direction == 'R':
        return Point(point.row, point.col + 1)

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
        head = Point(0, 0)
        tail = Point(0, 0)
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
        for _ in range(0, 10):
            points.append(Point(0, 0))

        seen = set()
        for raw_line in file.readlines():
            (direction, steps) = raw_line.strip().split()
            steps = int(steps)

            # move head
            for _ in range(0, steps):
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
                    points[pi] = Point(new_row, new_col)

        seen.add(points[-1])
        print(len(seen))

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