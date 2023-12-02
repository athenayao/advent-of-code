from collections import defaultdict
import sys
import os


ALLOWED_CUBES = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

def is_valid(game):
    for game_instance in game.split(";"):
        seen = defaultdict(int)
        cubes = [cube.strip().split(" ") for cube in game_instance.split(",")]
        for (count, key) in cubes:
            seen[key] += int(count)
            if seen[key] > ALLOWED_CUBES[key]:
                return False
    return True
    

def run(lines):
    total = 0
    for line in lines:
        game_meta, game_data = line.split(':')
        game_id = game_meta.split(' ')[-1]

        if is_valid(game_data.strip()):
            total += int(game_id)
            
    return total
            

        

if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        is_example = True
        filename = 'input-example.txt' if is_example else 'input.txt'
    with open(os.path.join(script_dir, filename), 'r') as f:
        answer = run(f.read().splitlines())
        print("### ANSWER ### ")
        print(answer)