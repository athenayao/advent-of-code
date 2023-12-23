#!/usr/bin/python3
from collections import defaultdict
import argparse
import sys
import os

def line_intersects(first, second):
    first_min = min(first)
    first_max = max(first)
    second_min = min(second)
    second_max = max(second)

    return (first_min <= second_min <= first_max) or (first_min <= second_max <= first_max) or (second_min <= first_min <= second_max) or (second_min <= first_max <= second_max)

class Brick:
    def __init__(self, end_1, end_2, brick_id):
        self.end_1 = end_1
        self.end_2 = end_2

        self.range_x = (end_1.x, end_2.x)
        self.range_y = (end_1.y, end_2.y)
        self.range_z = (end_1.z, end_2.z)
        self.sits_on = set()

        self.id = brick_id

    @staticmethod
    def parse(end_1_str, end_2_str, brick_id):
        end_1 = Coordinate.parse(end_1_str)
        end_2 = Coordinate.parse(end_2_str)
        return Brick(end_1, end_2, brick_id)

    def intersects(self, other):
        return line_intersects(self.range_x, other.range_x) and  line_intersects(self.range_y, other.range_y) and line_intersects(self.range_z, other.range_z)

        
    def __eq__(self, other):
        return self.range_x == other.range_x and self.range_y == other.range_y and self.range_z == other.range_z
        

    def __repr__(self):
        return f'{self.end_1}~{self.end_2}'

class Coordinate:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    @staticmethod
    def parse(string):
        x, y, z = string.split(',')
        return Coordinate(x, y, z)

    def __repr__(self):
        return f'({self.x},{self.y},{self.z})'

def run(lines):
    bricks = {}

    brick_id = 0
    # parse the bricks
    for line in lines:
        end_1, end_2 = line.split("~")
        brick = Brick.parse(end_1, end_2, brick_id)
        brick_id += 1
        bricks[brick_id] = brick
    
    # min or max? maybe it doesn't matter
    sorted_bricks = sorted(bricks.values(), key=lambda brick: min(brick.range_z))
    print("make them fall")

    # make them fall
    # what if we have a really tall brick... do we care about the bottom or the top? hmm. maybe the bottom
    # print("before:", bricks)
    supports = defaultdict(set)
    for i, falling_brick in enumerate(sorted_bricks):
        sits_on = set()
        current_brick = falling_brick
        hit_bottom = False
        # print(display[i], current_brick)

        while not hit_bottom:
            # we're already at the lowest point
            if current_brick.range_z[0] == 1 or current_brick.range_z[1] == 1:
                hit_bottom = True
                break
            one_down = Brick(Coordinate(current_brick.end_1.x, current_brick.end_1.y, current_brick.end_1.z - 1), Coordinate(current_brick.end_2.x, current_brick.end_2.y, current_brick.end_2.z - 1), current_brick.id)

            for j, other_brick in enumerate(bricks.values()):
                if i == j:
                    continue
                if one_down.intersects(other_brick):
                    hit_bottom = True
                    supports[other_brick.id].add(current_brick.id)
                    current_brick.sits_on.add(other_brick.id)
            if not hit_bottom:    
                current_brick = one_down
        bricks[i] = current_brick

    # and now we see how many things are affected
    print(supports)
    counter = 0
    for root_brick in [*supports.keys()]:
        print("ROOT_BRICK", root_brick)
        to_process = [root_brick]
        seen = set()
        import pdb; pdb.set_trace()
        while to_process:
            brick_id = to_process.pop(0)

            sits_on = bricks[brick_id].sits_on
            # if we have things we sit on that we haven't seen yet, that means we're supported in some way
            if brick_id in seen:
                continue
            seen.add(brick_id)
            to_process.extend([x for x in supports[brick_id]])
        counter += len(seen)
        print("initial brick id", root_brick, "ABCDEFG"[root_brick], len(seen))
    return counter

    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='run.py')
    parser.add_argument('-x', '--example', action='store_true')
    args = parser.parse_args()

    filename = 'input-example.txt' if args.example else 'input.txt'

    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, filename), 'r') as f:
        answer = run(f.read().splitlines())
        print("### ANSWER ### ")
        print(answer)
