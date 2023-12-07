#!/usr/bin/python3
import enum
import argparse
import sys
import os
from collections import defaultdict

card = {
    # f loops
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

class Type(enum.IntEnum):
    HIGH = 6
    ONE_PAIR = 5
    TWO_PAIR = 4
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 2
    FOUR_OF_A_KIND = 1
    FIVE_OF_A_KIND = 0

    @staticmethod
    def find_type(hand):
        count = defaultdict(int)
        for char in hand:
            count[char] += 1
        counted = sorted(count.values(), reverse=True)

        # probably more efficient as some kind of multiplied number. oh well
        first = counted[0]
        if first == 5:
            return Type.FIVE_OF_A_KIND
        if first == 4:
            return Type.FOUR_OF_A_KIND
        if first == 3:
            if len(counted) == 2:
                return Type.FULL_HOUSE
            else:
                return Type.THREE_OF_A_KIND
        if first == 2:
            if counted[1] == 2:
                return Type.TWO_PAIR
            return Type.ONE_PAIR
        return Type.HIGH

class Hand:
    def __init__(self, value, bid):
        self.value = value
        self.type = Type.find_type(sorted(value))
        self.bid = int(bid)
    
    def __repr__(self):
        return f'{self.type} [{self.value}]'


def hand_key(hand):
    key = [-1 * hand.type, *(card[v] for v in hand.value )]
    return key

def run(lines):
    hands = []
    for line in lines:
        (hand, bid) = line.split()
        hand = Hand(hand, bid)
        hands.append(hand)
    sorted_hands = sorted(hands, key=hand_key)

    total = 0
    for rank, hand in enumerate(sorted_hands, start=1):
        total += hand.bid * rank
    return total

        

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