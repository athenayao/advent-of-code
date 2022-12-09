def calculate_trees(lines, increment_x, increment_y):
    current_x = 0
    current_y = 0
    trees_encountered = 0
    max_x = len(lines[0])
    while True:
        current_x += increment_x 
        current_x %= max_x
        current_y += increment_y
        
        if current_y >= len(lines):
            break
            
        if lines[current_y][current_x] == '#':
            trees_encountered += 1
    return trees_encountered

def run(lines):
    inputs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    results = [calculate_trees(lines, value[0], value[1]) for value in inputs]
    print(results)
    total_value = 1
    for result in results:
        total_value *= result
    print(total_value)

if __name__ == '__main__':
    is_example = False
    with open('./input-example.txt' if is_example else './input.txt', 'r') as f:
        run(f.read().splitlines())