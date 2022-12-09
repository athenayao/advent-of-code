def run(lines):
    for line in lines:
        print(line)

if __name__ == '__main__':
    is_example = True
    with open('./input-example.txt' if is_example else './input.txt', 'r') as f:
        answer = run(f.read().splitlines())
        print("### ANSWER ### ")
        print(answer)
