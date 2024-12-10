#!/usr/bin/python3
from typing import TypeVar
from dataclasses import dataclass
import enum
import argparse
import sys
import os

EMPTY_SPAN = -1

class Mode(enum.Enum):
    FILE_LEN = 1
    FREE_SPACE = 2

Span = TypeVar("Span")

@dataclass
class Span:
    length: int
    file_id: int
    next_span: Span
    prev_span: Span

    def __init__(self, length, file_id):
        self.length = length
        self.file_id = file_id
        self.next_span = None
        self.prev_span = None
    
    def __repr__(self):
        if self.file_id == -1:
            return '.' * self.length
        return str(self.file_id) * self.length
    
    def is_empty(self):
        return self.file_id == EMPTY_SPAN
    
    def replace(self, other_span):
        self.next_span = other_span.next_span
        self.next_span.prev_span = self

        other_span.prev_span.next_span = self

    def insert_next(self, other_span):
        other_span.next_span = self.next_span
        self.next_span.prev_span = other_span
        self.next_span = other_span
        other_span.prev_span = self


def calculate_checksum(root_span):
    # multiply block position by the file number
    checksum = 0
    idx = 0
    
    current_span = root_span
    while current_span:
        if current_span.is_empty():
            idx += current_span.length
        else:
            for _ in range(0, current_span.length):
                checksum += idx * current_span.file_id
                idx += 1
        current_span = current_span.next_span
    return checksum
        

def print_line(root):
    cur_span = root
    results = []
    while cur_span:
        results.append(str(cur_span))
        cur_span = cur_span.next_span
    print("".join(results))

def find_file_id(root, file_id):
    # now find the next processed
    cur_span = root
    while cur_span:
        if cur_span.file_id == file_id:
           break
        cur_span = cur_span.next_span
    return cur_span

# i suspect my problem is what happens when we have multiple digits...
# but it worked for part 1!! so maybe not
def run(lines):
    file_id = 0

    root = None
    current_span = None
    prev_span = None

    for line in lines:
        for idx, length in enumerate(line):
            length = int(length)
            if idx % 2 == 0:
                span = Span(length, file_id)
                file_id += 1
            else:
                span = Span(length, EMPTY_SPAN)
    
            if root is None:
                root = span

            prev_span = current_span
            current_span = span
            if prev_span:
                prev_span.next_span = current_span
                current_span.prev_span = prev_span

    moving_span = find_file_id(root, file_id - 1)
    current_span = root
    prev_span = None
    new_span = None
    print_line(root)

    current_file_id = moving_span.file_id

    while current_file_id >= 0:
        front_cursor = root
        while front_cursor:
            if front_cursor.file_id == moving_span.file_id:
                break

            if not front_cursor.is_empty():
                front_cursor = front_cursor.next_span
                continue

            if front_cursor.length >= moving_span.length:
                new_span_length = min(front_cursor.length, moving_span.length)

                # "move" moving span
                new_span = Span(new_span_length, moving_span.file_id)
                new_span.replace(front_cursor)
                moving_span.file_id = EMPTY_SPAN
                
                empty_span_length = front_cursor.length - new_span_length

                if empty_span_length > 0:
                    new_empty_span =  Span(empty_span_length, EMPTY_SPAN)
                    new_span.insert_next(new_empty_span)

                break

            front_cursor = front_cursor.next_span

        # now find the next processed
        current_file_id -= 1
        moving_span = find_file_id(root, current_file_id)
            
    print_line(root)
    return calculate_checksum(root)

        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='run.py')
    parser.add_argument('-x', '--example', action='store_true')
    args = parser.parse_args()

    filename = 'input-example.txt' if args.example else 'input.txt'

    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, filename), 'r') as f:
        answer = run(f.read().splitlines())
        print("### ANSWER ### ")
        print(answer)