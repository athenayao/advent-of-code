import os
import collections
from itertools import permutations

ACTIVE = '#'
INACTIVE = '.'

POSSIBLE_DELTAS = [-1, 0, 1]
NUM_DIMENSIONS = 3

def to_key(dimensions):
    return ":".join([str(dim) for dim in dimensions])

def to_point(key):
    return [int(dim) for dim in key.split(":")]

def is_active(grid, point_delta):
    return 1


def get_deltas(dimensions):
    if len(dimensions) == 0:
        return [[]]
    
    to_return = []
    for results in get_deltas(dimensions[1:]):
        for possible_delta in POSSIBLE_DELTAS:
            to_return.append(results + [possible_delta])
    return to_return
    

def count_active_neighbors(grid, point):
    count = 0
    dimensions = [None] * 3
    neighbors = []
    deltas = get_deltas(dimensions)

    for delta in deltas:
        if len(list(filter(lambda d: d != 0, delta))) == 0:
            continue

        new_point = []
        for i, dim in enumerate(point):
            new_point.append(dim + delta[i])

        # TODO
        if grid.get(to_key(new_point), None) == ACTIVE:
            count += 1

    return count


def update_grid(grid):
    new_grid = {}

    # lazy: hardcoding 3 dimensions
    default = {'min': 0, 'max': 0}
    edges = [{'min': 0, 'max': 0} for _ in range(NUM_DIMENSIONS)]
    for key in grid.keys():
        point = to_point(key)
        for i, dimension in enumerate(point):
            edges[i]['min'] = min(edges[i]['min'], dimension)
            edges[i]['max'] = max(edges[i]['max'], dimension)    

    # get all edge points beyond currently known
    # this includes them whether they're active or not. likely inefficient
    processed = {}
    queue = list(grid.items())
    while len(queue) > 0:
        key, current = queue.pop()
        processed[key] = current

        point = to_point(key)
        for i, dim in enumerate(point):
            if dim == edges[i]['min']:
                point_copy = point.copy()
                point_copy[i] = dim - 1
                queue.append((to_key(point_copy), INACTIVE))
            if dim == edges[i]['max']:
                point_copy = point.copy()
                point_copy[i] = dim + 1
                queue.append((to_key(point_copy), INACTIVE))

        count = count_active_neighbors(grid, point)

        if current == ACTIVE:
            if count == 2 or count == 3:
                new_grid[key] = ACTIVE
            else:
                new_grid[key] = INACTIVE
        else:
            if count == 3:
                new_grid[key] = ACTIVE
            else:
                new_grid[key] = INACTIVE
    # print_grid(processed)
    # import pdb; pdb.set_trace()
    return new_grid


def print_grid(grid):
    z_grids = collections.defaultdict(dict)
    for key, item in grid.items():
        point = to_point(key)
        z_grids[point[2]][key] = item

    for z_key, z_slice in z_grids.items():
        print(f"\nz={z_key}", end="")
        sorted_keys = list(z_slice.keys())
        sorted_keys.sort(key=lambda x: to_point(x)[1])
        y_point = None
        for key in sorted_keys:
            value = z_slice[key]
            prev_y = y_point
            x_point, y_point, z_point = to_point(key)
            if prev_y != y_point:
                print("")
            print(value, end='')
            prev_y = y_point
        print("")


def run(lines):
    grid = {}
    for (y, line) in enumerate(lines):
        for (x, cell) in enumerate(line):
            grid[to_key([x, y, 0])] = cell
    
    # print_grid(grid)
    for _ in range(6):
        grid = update_grid(grid)
        # print_grid(grid)
    return len(list(filter(lambda x: x == ACTIVE, grid.values())))

if __name__ == '__main__':
    is_example = True
    script_dir = os.path.dirname(__file__)
    filename = 'input-example.txt' if is_example else 'input.txt'
    with open(os.path.join(script_dir, filename), 'r') as f:
        answer = run(f.read().splitlines())
        print("### ANSWER ### ")
        print(answer)
