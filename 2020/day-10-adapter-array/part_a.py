def run(lines):
    sorted_adapters = sorted([int(line) for line in lines])
    device_joltage = sorted_adapters[-1] + 3
    sorted_adapters.append(device_joltage)

    previous_joltage = 0
    one_jolt_diff = 0
    three_jolt_diff = 0
    for adapter in sorted_adapters:
        diff = adapter - previous_joltage
        if diff == 1:
            one_jolt_diff += 1
        elif diff == 3:
            three_jolt_diff += 1
        previous_joltage = adapter
    return one_jolt_diff * three_jolt_diff
        

if __name__ == '__main__':
    is_example = False
    with open('./input-example.txt' if is_example else './input.txt', 'r') as f:
        answer = run(f.read().splitlines())
        print("### ANSWER ### ")
        print(answer)
