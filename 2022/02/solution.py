#! python3
from optparse import OptionParser
import enum
import sys

class Moves(enum.Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


def calculate_match_score(opponent, player):
    # calculate who won
    diff = player.value - opponent.value
    abs_diff = abs(diff)

    # this is the edge case rock vs scissors
    if diff == 0:
        return 3 # tie
    elif abs_diff == 2:
        return 0 if diff > 0 else 6
    else:
        return 0 if diff < 0 else 6


def run_part_1(filename):
    with open(filename, 'r') as file:
        total = 0
        for raw_line in file.readlines():
            (opponent, player) = raw_line.strip().split()

            if opponent == 'A':
                opponent = Moves.ROCK
            elif opponent == 'B':
                opponent = Moves.PAPER
            elif opponent == 'C':
                opponent = Moves.SCISSORS

            if player == 'X':
                player = Moves.ROCK
            elif player == 'Y':
                player = Moves.PAPER
            elif player == 'Z':
                player = Moves.SCISSORS

            outcome = calculate_match_score(opponent, player)
            total += outcome + player.value + 1
        print(total)

        


def run_part_2(filename):
    with open(filename, 'r') as file:
        total = 0
        for raw_line in file.readlines():
            (opponent, outcome) = raw_line.strip().split()

            if opponent == 'A':
                opponent = Moves.ROCK
            elif opponent == 'B':
                opponent = Moves.PAPER
            elif opponent == 'C':
                opponent = Moves.SCISSORS

            score = 0
            if outcome == 'Y':
                # draw
                player = opponent.value
                score = 3
            elif outcome == 'X':
                # lose
                player = ((opponent.value - 1) % 3) 
                score = 0
            else:
                # win
                player = ((opponent.value + 1) % 3)
                score = 6

            sum = player + score + 1
            total += sum
        print(total)
        
            

if __name__ == '__main__':
    mode = sys.argv[1]
    if not mode:
        mode == "1a"

    if mode == "1a":
        run_part_1('./sample-input.txt')
    elif mode == "1b":
        run_part_1("./input.txt")
    elif mode == "2a":
        run_part_2('./sample-input.txt')
    else:
        run_part_2('./input.txt')