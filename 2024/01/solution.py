#!/usr/bin/env python3
# https://adventofcode.com/2024/day/1

from pathlib import Path

FILE = "input.txt"
# FILE = "sample.txt"


def main():
    data = load_input()
    print(f"PART 1: {solve_part_1(data)}")
    print(f"PART 2: {solve_part_2(data)}")


def load_input(file=FILE) -> list:
    path = Path(__file__).with_name(file)
    with open(path, "r") as f:
        return [line.strip() for line in f]


def solve_part_1(data):
    lefts, rights = [], []
    for line in data:

        left, right = line.split(' ', 1)
        lefts.append(int(left.strip()))
        rights.append(int(right.strip()))
    
    pairs = [
        (left, right)
        for left, right
        in zip(sorted(lefts), sorted(rights))
    ]

    diffs = []

    for a, b in pairs:
        diff = a - b
        diffs.append(abs(diff))

    return sum(diffs)



def solve_part_2(data):
    lefts, rights = [], []
    for line in data:
        left, right = line.split(' ', 1)
        lefts.append(int(left.strip()))
        rights.append(int(right.strip()))

    score = 0

    for left in lefts:
        for right in rights:
            if left == right:
                score += left
    
    return score

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
