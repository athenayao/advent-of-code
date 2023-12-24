#!/usr/bin/python3
import argparse
import sys
import os


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'({self.x}, {self.y}, {self.z})'

class Line:
    def __init__(self, p1, p2, y_delta):
        self.p1 = p1
        self.p2 = p2
        self.y_delta = y_delta

    def intersects(self, other):
        # parallel

        x1 = self.p1.x
        x2 = self.p2.x
        x3 = other.p1.x
        x4 = other.p2.x
        y1 = self.p1.y
        y2 = self.p2.y
        y3 = other.p1.y
        y4 = other.p2.y

        intersection_x_numerator = ((((x1 * y2)-(y1 * x2)) * (x3 - x4)) - ((x1 - x2) * ((x3 * y4) - y3 * x4)))
        intersection_y_numerator = ((((x1 * y2)-(y1 * x2)) * (y3 - y4)) - ((y1 - y2) * ((x3 * y4) - y3 * x4)))
        denominator = ((x1-x2)*(y3-y4)) - ((y1-y2) * (x3-x4))

        # parallel
        if denominator == 0:
            return None
        return Point(intersection_x_numerator / denominator, intersection_y_numerator / denominator, 0)

    @staticmethod
    def parse(point_string, slope_string):
        (x, y, z) = [int(thing.strip()) for thing in point_string.split(",")]
        (x_delta, y_delta, z_delta) = [int(thing.strip()) for thing in slope_string.split(",")]
        p1 = Point(x, y, z)
        p2 = Point(x + x_delta, y + y_delta, z + z_delta)

        return Line(p1, p2, y_delta)
    
    def __repr__(self):
        return f'{self.p1}, {self.p2}'

    # def get_y_intercept(self):
    #     return (self.y - self.slope) * self.x

    # def intersects(self, other):
    #     a = self.slope
    #     c = self.y_intercept
    #     b = other.slope
    #     d = other.y_intercept
        
    #     # parallel
    #     if a == b:
    #         return False

    #     new_x = (d - c) / (a - b)
    #     new_y = (a * new_x) + c

    #     # handle if it's in the past
    #     print(new_x, new_y)
    #     return True


def intersection_is_in_past(line, intersection):
    y_delta = line.y_delta
    
    if y_delta > 0:
        return intersection.y < line.p1.y
    
    if y_delta < 0:
        return intersection.y > line.p1.y
    
    # ehhhhh did I get lucky
    if y_delta == 0:
        print("slope is 0!", line)
        return True

def run(inputs, min_test, max_test):
    lines = []
    for l in inputs:
        line = Line.parse(*l.split("@"))
        lines.append(line)

    counter = 0
    for i, line1 in enumerate(lines):
        for j in range(i+1, len(lines)):
            line2 = lines[j]
            intersection = line1.intersects(line2)
            # parallel
            if not intersection:
                print(line1.p1, line2.p1, "parallel")
                continue

            # outside test area
            if not ((min_test <= intersection.x <= max_test) and (min_test <= intersection.y <= max_test)):
                print(line1.p1, line2.p1, "outside")
                continue
            
            # is in the past
            if intersection_is_in_past(line1, intersection) and intersection_is_in_past(line2, intersection):
                print(line1.p1, line2.p1, "past, line 1 and line 2")
                continue
            if intersection_is_in_past(line1, intersection):
                print(line1.p1, "past, line 1")
                continue
            
            if intersection_is_in_past(line2, intersection):
                print(line2.p1, "past, line 2")
                continue

            print(line1.p1, line2.p1, intersection)
            counter += 1
    return counter                

if __name__ == '__main__':
    # import pdb; pdb.set_trace()
    parser = argparse.ArgumentParser(prog='run.py')
    parser.add_argument('-x', '--example', action='store_true')
    args = parser.parse_args()

    filename = 'input-example.txt' if args.example else 'input.txt'
    min_test = 7 if args.example else 200000000000000
    max_test = 27 if args.example else 400000000000000

    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, filename), 'r') as f:
        answer = run(f.read().splitlines(), min_test, max_test)
        print("### ANSWER ### ")
        print(answer)