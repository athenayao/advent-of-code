#!/usr/bin/python3
from collections import namedtuple
import argparse
import sys
import os

START = 'S'

Point = namedtuple('Point', 'y, x')
class Pipe:
    def __init__(self, tile, y, x, north=None, south=None, east=None, west=None):
        self.tile = tile
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.seen = False
        self.x = x
        self.y = y
        self.distance = 0

    def __repr__(self):
        directions = ''
        if self.north:
            directions += 'N'
        if self.south:
            directions += 'S'
        if self.west:
            directions += 'W'
        if self.east:
            directions += 'E'
        return f'{self.tile} ({directions})'
    
    

def make_key(y, x):
    return f'{y}.{x}'


def find_connections(tile, y, x):
    if tile == '|':
        return Pipe(tile, y, x, north=True, south=True)
    if tile == '-':
        return Pipe(tile, y, x, east=True, west=True)
    if tile == 'L':
        return Pipe(tile, y, x, north=True, east=True)
    if tile == 'J':
        return Pipe(tile, y, x, north=True, west=True)
    if tile == '7':
        return Pipe(tile, y, x, south=True, west=True)
    if tile == 'F':
        return Pipe(tile, y, x, south=True, east=True)


def has_connection(pipe, direction):
    if pipe is None:
        return False
    if direction == 'north':
        return getattr(pipe, 'south')
    if direction == 'south':
        return getattr(pipe, 'north')
    if direction == 'east':
        return getattr(pipe, 'west')
    if direction == 'west':
        return getattr(pipe, 'east')
    


start_y = None
start_x = None
def run(lines):
    nodes = {}

    # y.x = char
    pipes = {}
    # just finding the S

    first_line = '.' * (len(lines[0]) + 2)
    padded_lines = [first_line, *[f'.{line}.' for line in lines], first_line]
    for y, line in enumerate(padded_lines):
        for x, char in enumerate(list(line)):
            if char == '.':
                continue
            pipes[f'{y}.{x}'] = find_connections(char, y, x)
            if char == 'S':
                start_y = y
                start_x = x
    
    start_pipe = Pipe('S', start_y, start_x,
            north=has_connection(pipes.get(f'{start_y-1}.{start_x}'), 'north'),
            south=has_connection(pipes.get(f'{start_y+1}.{start_x}'), 'south'),
            east=has_connection(pipes.get(f'{start_y}.{start_x+1}'), 'east'),
            west=has_connection(pipes.get(f'{start_y}.{start_x-1}'), 'west'),
    )
    
    pipes[f'{start_y}.{start_x}'] = start_pipe

    loop_length = 0
    pipe = start_pipe
    while pipe:
        pipe.seen = True

        # find next
        # y - 1, y + 1, x - 1, x + 1
        new_x = pipe.x
        new_y = pipe.y
        new_pipe = None
        # import pdb; pdb.set_trace()
        if not new_pipe and pipe.south:
            new_pipe = pipes.get(make_key(pipe.y + 1, pipe.x))
            if new_pipe.seen:
                new_pipe = None
            
        if not new_pipe and pipe.north:
            new_pipe = pipes.get(make_key(pipe.y - 1, pipe.x))
            if new_pipe.seen:
                new_pipe = None

        if not new_pipe and pipe.east:
            new_pipe = pipes.get(make_key(pipe.y, pipe.x + 1))
            if new_pipe.seen:
                new_pipe = None
        
        if not new_pipe and pipe.west:
            new_pipe = pipes.get(make_key(pipe.y, pipe.x - 1))
            if new_pipe.seen:
                new_pipe = None

        pipe.distance = loop_length
        pipe = new_pipe
        loop_length += 1
        print(pipe)

    return loop_length // 2
            


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