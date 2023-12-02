from collections import defaultdict
import sys
import os

def process(game):
    current_max = defaultdict(int)
    for game_instance in game.split(";"):
        cubes = [cube.strip().split(" ") for cube in game_instance.split(",")]
        for (count, key) in cubes:
            current_max[key] = max(current_max[key], int(count))
    power = 1
    for x in current_max.values():
        power *= x
    return power

    

def run(lines):
    total = 0
    for line in lines:
        game_meta, game_data = line.split(':')
        game_id = game_meta.split(' ')[-1]

        total += process(game_data.strip())
            
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