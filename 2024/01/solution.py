#!/usr/bin/env python3
# https://adventofcode.com/2024/day/1

from pathlib import Path
from re import split

FILE = "input.txt"
# FILE = "sample.txt"


def main():
    data = load_input()
    print(f"PART 1: {solve_part_1(data)}")
    print(f"PART 2: {solve_part_2(data)}")


def load_input(file: str = FILE) -> list:
    path = Path(__file__).with_name(file)
    with open(path, "r") as f:
        return [line.strip() for line in f]


def split_lines(lines: list) -> tuple[list]:
    lefts, rights = [], []

    for line in lines:
        left, right = line.split()
        lefts.append(int(left))
        rights.append(int(right))
    
    return sorted(lefts), sorted(rights)

def solve_part_1(data: list) -> int:
    total = 0

    for a, b in zip(*split_lines(data)):
        total += abs(a - b)

    return total


def solve_part_2(data: list) -> int:
    lefts, rights = split_lines(data)
    score = 0
    for a in lefts:
        for b in rights:
            if a == b:
                score += a
    
    return score

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
