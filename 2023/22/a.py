#!/usr/bin/python3
import argparse
import sys
import os

def line_intersects(first, second):
    first_min = min(first)
    first_max = max(first)
    second_min = min(second)
    second_max = max(second)

    return (first_min <= second_min <= first_max ) or (first_min <= second_max <= first_max) or (second_min <= first_min <= second_max) or (second_min <= first_max <= second_max)

class Brick:
    def __init__(self, end_1, end_2):
        self.end_1 = end_1
        self.end_2 = end_2

        self.range_x = (end_1.x, end_2.x)
        self.range_y = (end_1.y, end_2.y)
        self.range_z = (end_1.z, end_2.z)

    @staticmethod
    def parse(end_1_str, end_2_str):
        end_1 = Coordinate.parse(end_1_str)
        end_2 = Coordinate.parse(end_2_str)
        return Brick(end_1, end_2)

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


def test():
    bricks = [
        (Brick.parse('(2,2,2)', '(2,2,2)'), Brick.parse('(2,2,2)', '(2,2,2)')),
        (Brick.parse('(2,2,2)', '(2,2,2)'), Brick.parse('(1,1,1)', '(1,1,1)')),
        (Brick.parse('(2,2,2)', '(3,3,3)'), Brick.parse('(3,4,3)', '(4,4,4)')),
        (Brick.parse('(2,2,2)', '(3,3,3)'), Brick.parse('(3,2,3)', '(4,4,4)')),
    ]
    for brick_1, brick_2 in bricks:
        print(brick_1, brick_2, brick_1.intersects(brick_2), brick_2.intersects(brick_1))

display = 'ABCDEFG'
def can_disintegrate(bricks, brick_index):
    did_descend = False
    # if brick_index == 5:
    #     import pdb; pdb.set_trace()

    for i, falling_brick in enumerate(bricks):
        # print("NOW FALLING",falling_brick)
        if i == brick_index:
            continue
        intersects = False

        # we don't need a loop here
        # we're already at the lowest point
        if falling_brick.range_z[0] == 1 or falling_brick.range_z[1] == 1:
            continue
        one_down = Brick(Coordinate(falling_brick.end_1.x, falling_brick.end_1.y, falling_brick.end_1.z - 1), Coordinate(falling_brick.end_2.x, falling_brick.end_2.y, falling_brick.end_2.z - 1))

        for j, other_brick in enumerate(bricks):
            if i == j or j == brick_index:
                continue
            # print(f"{one_down} intersects {other_brick}? " ,one_down.intersects(other_brick))
            # import pdb; pdb.set_trace()
            if one_down.intersects(other_brick):
                intersects = True
                break

        if not intersects:
            did_descend = True
            break

    # print(display[brick_index], bricks[brick_index], not did_descend)
    return not did_descend

def run(lines):
    bricks = []

    # parse the bricks
    for line in lines:
        end_1, end_2 = line.split("~")
        brick = Brick.parse(end_1, end_2)
        bricks.append(brick)
    
    # min or max? maybe it doesn't matter
    bricks = sorted(bricks, key=lambda brick: min(brick.range_z))
    print("make them fall")

    # make them fall
    # what if we have a really tall brick... do we care about the bottom or the top? hmm. maybe the bottom
    # print("before:", bricks)
    for i, falling_brick in enumerate(bricks):
        current_brick = falling_brick
        hit_bottom = False
        # print(display[i], current_brick)

        while not hit_bottom:
            # we're already at the lowest point
            if current_brick.range_z[0] == 1 or current_brick.range_z[1] == 1:
                hit_bottom = True
                break
            one_down = Brick(Coordinate(current_brick.end_1.x, current_brick.end_1.y, current_brick.end_1.z - 1), Coordinate(current_brick.end_2.x, current_brick.end_2.y, current_brick.end_2.z - 1))

            for j, other_brick in enumerate(bricks):
                if i == j:
                    continue
                # print(f"{one_down} intersects {other_brick}? " ,one_down.intersects(other_brick))
                if one_down.intersects(other_brick):
                    hit_bottom = True
                    # print("we just hit bottom", current_brick, one_down)
                    break
            if not hit_bottom:    
                current_brick = one_down
            
        bricks[i] = current_brick
    
    print("now disintegrate")
    # now we disintegrate bricks
    # print("after: ", bricks)
    count = 0
    for i in range(0, len(bricks)):
        # print("processing", bricks[i])
        if can_disintegrate(bricks, i):
            count += 1
    return count

    

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
