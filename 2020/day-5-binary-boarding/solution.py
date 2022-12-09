import math

def binary_search(array, range):
    print(array, range)

def find_seat(line):
    row = None
    seat = None

    row_start = 0
    row_end = 127
    seat_start = 0
    seat_end = 7
    for char in line:
        if char == 'F' or char == 'B':
            if char == 'F':
                row_end = math.floor((row_end + row_start) / 2)
            elif char == 'B':
                row_start = math.ceil((row_end + row_start) / 2)
            if row_start == row_end:
                row = row_start
    
        if char == 'L' or char == 'R':
            if char == 'L':
                seat_end = math.floor((seat_end + seat_start) / 2)
            elif char == 'R':
                seat_start = math.ceil((seat_end + seat_start) / 2)
            if seat_end == seat_start:
                seat = seat_start
    # print(row, seat, row * 8 + seat)
    return row * 8 + seat

def run(lines):
    seat_ids = []
    for line in lines:
        seat_ids.append(find_seat(line))

    sorted_seats = sorted(seat_ids)
    previous_seat_id = None
    for index, seat_id in enumerate(sorted_seats):
        if previous_seat_id is not None and seat_id - previous_seat_id == 2:
            print(seat_id, previous_seat_id)
        previous_seat_id = seat_id
        

if __name__ == '__main__':
    is_example = False
    with open('./input-example.txt' if is_example else './input.txt', 'r') as f:
        run(f.read().splitlines())