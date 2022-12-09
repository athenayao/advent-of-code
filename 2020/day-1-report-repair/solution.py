def run(lines):
    numbers = [int(line.rstrip()) for line in lines]
    for first_index in range(0, len(numbers)):
        for second_index in range(first_index + 1, len(numbers)):
            for third_index in range(second_index + 1, len(numbers)):

                if numbers[first_index] + numbers[second_index] + numbers[third_index] == 2020:
                    print(numbers[first_index] * numbers[second_index] * numbers[third_index])
                    return


if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        run(f.readlines())

    