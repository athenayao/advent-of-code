#! /Users/athena/.nix-profile/bin/python

def run(filename):
    with open(filename, 'r') as file:
        for raw_line in file.readlines():
            line = raw_line.strip()
            print(".." + line)
            # do something

if __name__ == '__main__':
    run('./sample-input.txt')
    # run ('./input.txt')