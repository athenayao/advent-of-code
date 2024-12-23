#!/usr/bin/python3
import argparse
import sys
import os


def next_secret_number(secret_number):
    #            1 
    #      1000000
    # mix: 1000001
    print(bin(secret_number), secret_number)
    print(bin(secret_number << 6))
    secret_number = mix(secret_number, secret_number << 6)    
    print(bin(secret_number), secret_number)
    secret_number = prune(secret_number)
    print(bin(secret_number), secret_number)
    print(".")

    #       1000001
    #            10
    #       1000011
    print(bin(secret_number), secret_number)
    print(bin(secret_number >> 5))
    secret_number = mix(secret_number, secret_number >> 5)
    print(bin(secret_number), secret_number)
    secret_number = prune(secret_number)
    print(bin(secret_number), secret_number)
    print('..')

    #            1000011
    # 100001100000000000
    # 100001100001000011
    print(bin(secret_number), secret_number)
    print(bin(secret_number << 11))
    secret_number = mix(secret_number, secret_number << 11)
    print(bin(secret_number), secret_number)
    secret_number = prune(secret_number)
    print(bin(secret_number), secret_number)
    print('...')

    # 0b      100001100001000011 137283
    # 0b100001100001000011000000
    # 0b100001000000100010000011 8652931
    # 0b100001000000100010000011 8652931
    # .
    # 0b100001000000100010000011 8652931
    # 0b1000010000001000100
    # 0b100000000010100011000111 8399047
    # 0b100000000010100011000111 8399047
    # ..
    # 0b100000000010100011000111 8399047
    # 0b10000000001010001100011100000000000
    # 0b10000000001110001100001000011000111 17209626823
    # 0b110001100001000011000111 12980423
    import pdb; pdb.set_trace()
    return secret_number

def mix(n1, n2):
    return n1 ^ n2

def prune(secret_number):
    # 0b1000000000000000000000000
    # 2 ^ 24
    return secret_number % 16777216


def binary_secret_number(binary):
    pass
    



def run(lines):
    sum = 0
    for line in lines:
        secret_number = int(line)
        binary = bin(secret_number)[2:]

        for _ in range(0, 2000):
            secret_number = next_secret_number(secret_number)
            binary = binary_secret_number(binary)

        sum += secret_number
    return sum

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