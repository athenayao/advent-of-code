#!/usr/bin/python3
from typing import List
from dataclasses import dataclass
from enum import Enum
import argparse
import sys
import os


# instructions
class Instructions(Enum):
    adv = 0 # division      self.a
    bxl = 1 # bitwise xor   literal
    bst = 2 # % 8           combo
    jnz = 3 # infinite loop until 0
    bxc = 4 # bitwise xor   self.b self.c
    out = 5 # % 8 + output  combo
    bdv = 6 # division      self.b
    cdv = 7 # division      self.c 

# operands
# Combo operands 0 through 3 represent literal values 0 through 3.
# Combo operand 4 represents the value of register A.
# Combo operand 5 represents the value of register B.
# Combo operand 6 represents the value of register C.
# Combo operand 7 is reserved and will not appear in valid programs.

@dataclass
class Program:
    a: int
    b: int
    c: int
    instructions: List[int]
    output: List[int]

    pointer: int = 0

    def get_combo_value(self, raw_value):
        if raw_value == 0 or raw_value == 1 or raw_value == 2 or raw_value == 3:
            return raw_value
        if raw_value == 4:
            return self.a
        if raw_value == 5:
            return self.b
        if raw_value == 6:
            return self.c
        if raw_value == 7:
            assert False, "This should not happen in valid programs"

    def run(self):
        print(self)
        binary = []
        i = 0
        while i < len(self.instructions):
            next_output = self.instructions[i]
            binary.append(bin(next_output)[2:])
            print(next_output, binary)
            i += 1
            

        # while self.pointer < len(self.instructions):
        #     instr = self.instructions[self.pointer]
        #     operand = self.instructions[self.pointer + 1]
        #     # print("  ", self, instr, operand)
        #     # import pdb; pdb.set_trace()
        #     if instr == 0:
        #         self.adv(self.get_combo_value(operand))
        #     elif instr == 1:
        #         self.bxl(operand)
        #     elif instr == 2:
        #         self.bst(self.get_combo_value(operand))
        #     elif instr == 3:
        #         self.jnz(operand)
        #     elif instr == 4:
        #         self.bxc(operand)
        #     elif instr == 5:
        #         self.out(self.get_combo_value(operand))
        #         print(self.output)
        #         print(bin(self.a))
        #     elif instr == 6:
        #         self.bdv(self.get_combo_value(operand))
        #     elif instr == 7: 
        #         self.cdv(self.get_combo_value(operand))
        #     print(binary)
        # # print(self)
            


    def adv(self, combo):
        print(f"adv: self.a = self.a // 2 ** {combo}")
        # division
        numerator = self.a
        denominator = 2 ** combo
        self.a = numerator // denominator
        self.pointer += 2
    
    def bxl(self, combo):
        print(f"bxl: b^={combo}" )
        self.b ^= combo
        self.pointer += 2

    def bst(self, combo):
        print(f"bst: self.b = {combo} % 8")
        self.b = combo % 8
        self.pointer += 2

    def jnz(self, combo):
        print("jnz:", combo)
        if self.a == 0:
            self.pointer += 2
            return
        self.pointer = combo

    def bxc(self, _):
        print("bxc: self.b ^ self.c")
        self.b = self.b ^ self.c
        self.pointer += 2
    
    def out(self, combo):
        print(f"out: {combo} % 8")
        result = combo % 8
        self.output.append(result)
        self.pointer += 2

    def bdv(self, combo):
        print(f"bdv: self.b = self.a // 2 ** {combo}")
        numerator = self.a
        denominator = 2 ** combo
        self.b = numerator // denominator
        self.pointer += 2

    def cdv(self, combo):
        print(f"cdv: self.c = self.a // 2 ** {combo}")
        numerator = self.a
        denominator = 2 ** combo
        self.c = numerator // denominator
        self.pointer += 2

def run(lines):
    [_, a] = lines[0].split(":")
    [_, b] = lines[1].split(":")
    [_, c] = lines[2].split(":")
    [_, program] = lines[4].split(":")

    program = Program(int(a), int(b), int(c), [int(x) for x in program.split(",")], [])
    program.run()
    print(program)
    return ",".join([str(x) for x in program.output])

    # program.run()


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