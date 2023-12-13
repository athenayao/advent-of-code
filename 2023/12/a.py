#!/usr/bin/python3
import re
import enum
from collections import namedtuple
import argparse
import sys
import os

DAMAGED = '#'
UNKNOWN = '?'
WORKING = '.'

class Chunk:
    def __init__(self, state, length):
        self.state = state
        self.length = length
    
    @property
    def raw(self):
        return self.state  * self.length

    @property
    def damaged(self):
        return self.state == DAMAGED

    @property
    def unknown(self):
        return self.state == UNKNOWN
    
    @property
    def working(self):
        return self.state == WORKING

    def __repr__(self):
        return self.raw

class Num:
    def __init__(self, value):
        self.value = value
        self.known = False

class State(enum.Enum):
    KNOWN = enum.auto()
    IN_UNKNOWN = enum.auto()

def find_arrangements(chunks, checknums):
    check_index = 0

    # state = State.KNOWN

    # for chunk in chunks:
    #     if chunk.working:
    #         if state == State.KNOWN:
    #             continue
    #         else:
    #             # TODO: need to do something if we're grouping
    #             pass

    #     if chunk.damaged:
    #         if state == State.KNOWN:
    #             if chunk.length == checknums[check_index]:
    #                 check_index += 1
    #                 continue
    #             else:
    #                 print("ERROR NOT MATCHING", chunk, checknums[check_index])
    #         else:
    #             # TODO
    #             pass
        
    #     if chunk.unknown:
    #         state = State.UNKNOWN
    #         # then what

        
        

def run(lines):
    for line in lines:
        springs, check = line.split()
        chunks = []
        current = None
        current_chunk = []
        for char in list(springs):
            if current and current != char:
                chunks.append(Chunk(state=current, length=len(current_chunk)))
                current_chunk = []
                current = None

            if current is None:
                current = char
            current_chunk.append(char)
        chunks.append(Chunk(state=current, length=len(current_chunk)))

        checknums = [int(i) for i in check.split(',')]

        print(find_arrangements(chunks, checknums))

            



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