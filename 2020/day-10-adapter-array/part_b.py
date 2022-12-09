cached_results = {}

def find_chain(adapters, chain):
    cached = cached_results.get(adapters[0], None)
    if cached  is not None:
        return cached

    if len(adapters) == 1:
        return 1

    count = 0
    for i in range(1, len(adapters)):
        if adapters[i] - adapters[0] > 3:
            continue
        current_chain = chain.copy()
        current_chain.append(adapters[0])
        count += find_chain(adapters[i:], current_chain)
    cached_results[adapters[0]] = count;
    return count

def run(lines):
    sorted_adapters = sorted([int(line) for line in lines])
    full_chain = [0]
    full_chain.extend(sorted_adapters)
    return find_chain(full_chain, [])

if __name__ == '__main__':
    is_example = False
    with open('./input-example.txt' if is_example else './input.txt', 'r') as f:
        answer = run(f.read().splitlines())
        print("### ANSWER ### ")
        print(answer)
