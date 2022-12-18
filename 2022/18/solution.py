#! python3
import sys
from collections import defaultdict

class Cube:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.free_side = 6
        self.visible_side = 0


    def tuple(self):
        return (self.x, self.y, self.z)



def hashkey(tuple):
    return ':'.join([str(x) for x in tuple])

def run_part_1(filename):
    with open(filename, 'r') as file:
        cubes = {}
        for raw_line in file.readlines():
            (x, y, z) = [int(num) for num in raw_line.strip().split(",")]
            cube = Cube(x, y, z)
            cubes[hashkey(cube.tuple())] = cube
        
        for cube in cubes.values():
            for point in get_adjacent(cube):
                key = hashkey(point)
                if key in cubes:
                    cubes[key].free_side -= 1

        total = 0
        for cube in cubes.values():
            total += cube.free_side
        print(total)


def get_adjacent(cube):
    return [
                (cube.x, cube.y, cube.z-1),
                (cube.x, cube.y, cube.z+1),
                (cube.x, cube.y-1, cube.z),
                (cube.x, cube.y+1, cube.z),
                (cube.x-1, cube.y, cube.z),
                (cube.x+1, cube.y, cube.z),
            ]

def run_part_2(filename):
    with open(filename, 'r') as file:
        cubes = {}

        min_x = float('inf')
        min_y = float('inf')
        min_z = float('inf')
        max_x = float('-inf')
        max_y = float('-inf')
        max_z = float('-inf')

        for raw_line in file.readlines():
            (x, y, z) = [int(num) for num in raw_line.strip().split(",")]
            cube = Cube(x, y, z)
            cubes[hashkey(cube.tuple())] = cube
        
            min_x = min(min_x, cube.x)
            min_y = min(min_y, cube.y)
            min_z = min(min_z, cube.z)

            max_x = max(max_x, cube.x)
            max_y = max(max_y, cube.y)
            max_z = max(max_z, cube.z)

        # check visible borders
        for cube in cubes.values():
            x_border = cube.x == min_x or cube.x == max_x
            y_border = cube.y == min_y or cube.y == max_y
            z_border = cube.z == min_z or cube.z == max_z
            if not (x_border or y_border or z_border):
                continue

            for point in get_adjacent(cube):
                if point[0] == cube.x:
                    
                # (cube.x, cube.y, cube.z-1),
                # (cube.x, cube.y, cube.z+1),
                # (cube.x, cube.y-1, cube.z),
                # (cube.x, cube.y+1, cube.z),
                # (cube.x-1, cube.y, cube.z),
                # (cube.x+1, cube.y, cube.z),


            # for point in get_adjacent(cube):
                # key = hashkey(point)
                
                # y_border = point[1] > min_y and point[1] < max_y
                # z_border = point[2] > min_z and point[2] < max_z
                # if not (x_border or y_border or z_border):
                #     print("bye free side", cube.tuple())
                #     cube.free_side -= 1
                #     continue
                # if key in cubes:
                #     cubes[key].free_side -= 1

        total = 0
        print(min_x, min_y)
        for cube in cubes.values():
            print(cube.tuple(), cube.free_side)
            total += cube.free_side
        print(total)


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else None
    if not mode:
        mode == "ax"

    if mode == "ax":
        run_part_1('./example.txt')
    elif mode == "a":
        run_part_1("./input.txt")
    elif mode == "bx":
        run_part_2('./example.txt')
    elif mode == "b":
        run_part_2('./input.txt')