#!/usr/bin/python3
from collections import defaultdict
import argparse
import sys
import os

def is_valid(page_order, pages):
    valid_pages = set(pages)
    seen_pages = set()

    for page in pages:
        required_pages = page_order[page]
        for required_page in required_pages:
            if required_page not in valid_pages:
                # it's not in the pages we care about, ignore
                continue

            if required_page not in seen_pages:
                return False
                
        seen_pages.add(page)
    return True

def get_middle_element(array):
    middle_index = (len(array) - 1 )// 2
    return array[middle_index]

def find_required_page(page, page_order, seen, valid_pages):
    required_pages = page_order[page]
    found = []
    for required_page in required_pages:
        if required_page in seen:
            continue
    
        if required_page in valid_pages:
            found += find_required_page(required_page, page_order, seen, valid_pages)
    
    if page not in seen:
        found += [page]
        seen.add(page)
    return found
    

def reorder_pages(page_order, pages):
    valid_pages = set(pages)
    seen = set()
    new_pages = []

    for page in pages:
        new_pages += find_required_page(page, page_order, seen, valid_pages)
        # print(pages, "->", new_pages)
    return new_pages

def run(lines):
    step = 1
    page_order = defaultdict(set)
    sum = 0
    for line in lines:
        if line == '':
            step += 1
            continue

        if step == 1:
            before, after = line.split("|")
            page_order[after].add(before)
        
        if step == 2:
            pages = line.split(",")
    
            if is_valid(page_order, pages):
                continue

            pages = reorder_pages(page_order, pages)
            
            sum += int(get_middle_element(pages), 10) 
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