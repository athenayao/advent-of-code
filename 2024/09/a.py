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
        if not current_span.is_empty():
            for _ in range(0, current_span.length):
                checksum += idx * current_span.file_id
                idx += 1
        current_span = current_span.next_span
    return checksum
        

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

    moving_span = current_span
    current_span = root
    prev_span = None
    new_span = None
    while current_span:
        if not current_span.next_span:
            break
        if current_span.is_empty():
            new_span_length = min(current_span.length, moving_span.length)

            # insert moving span
            new_span = Span(new_span_length, moving_span.file_id)
            new_span.replace(current_span)
            
            empty_span_length = current_span.length - new_span_length

            if empty_span_length > 0:
                new_empty_span =  Span(empty_span_length, EMPTY_SPAN)
                new_span.insert_next(new_empty_span)
                current_span = new_empty_span
            else:
                current_span = new_span

            moving_span_length = moving_span.length - new_span_length
            if moving_span_length < 0:
                print("SHOULDN'T HAPPEN ")
                break
            elif moving_span_length == 0:
                moving_span.prev_span.next_span = None
                # find next moving_span
                moving_span = moving_span.prev_span
                while moving_span.is_empty():
                    moving_span = moving_span.prev_span
            else:
                moving_span.length = moving_span_length
        else:
            current_span = current_span.next_span

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