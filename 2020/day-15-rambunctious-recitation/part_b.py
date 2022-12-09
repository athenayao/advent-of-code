import os
import collections

def run(lines):
    tracker = collections.defaultdict(list)
    numbers = [int(n) for n in lines[0].split(",")]
    counter = 0
    previously_spoken = False

    for number in numbers:
        counter += 1
        spoken = number
        tracker[spoken].append(counter)

    while True:
        counter += 1
        if len(tracker[spoken]) > 1:
            spoken = tracker[spoken][-1] - tracker[spoken][-2]
        else:
            spoken = 0
        tracker[spoken].append(counter)

        if counter == 30000000:
            return spoken

        
if __name__ == '__main__':
    # print(run(["1,3,2"]))
    # print(run(["2,1,3"]))
    # print(run(["1,2,3"]))
    # print(run(["2,3,1"]))
    # print(run(["3,2,1"]))
    # print(run(["3,1,2"]))
    
    is_example = False
    script_dir = os.path.dirname(__file__)
    filename = 'input-example.txt' if is_example else 'input.txt'
    with open(os.path.join(script_dir, filename), 'r') as f:
        answer = run(f.read().splitlines())
        print("### ANSWER ### ")
        print(answer)
