def parse_schedule(raw_schedule):
    return [int(bus) for bus in raw_schedule.split(",") if bus != 'x']

def find_my_bus(earliest_time, schedule):
    earliest_schedules = [(((earliest_time // bus) * bus) + bus, bus) for bus in schedule]
    return sorted(earliest_schedules)[0]

def run(lines):
    earliest_time = int(lines[0])
    schedule = parse_schedule(lines[1])
    (departure_time, bus) = find_my_bus(earliest_time, schedule)
    return (departure_time - earliest_time ) * bus
    

if __name__ == '__main__':
    is_example = False
    with open('./input-example.txt' if is_example else './input.txt', 'r') as f:
        answer = run(f.read().splitlines())
        print("### ANSWER ### ")
        print(answer)
