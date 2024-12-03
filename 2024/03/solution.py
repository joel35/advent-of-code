#!/usr/bin/env python3
# https://adventofcode.com/2024/day/3

from pathlib import Path
import re

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


def solve_part_1(data: list) -> int:
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'    
    total = 0

    for line in data:
        for a, b in re.findall(pattern, line):
            total += int(a) * int(b)

    return total


def solve_part_2(data: list) -> int:
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do(?:n\'t)?"
    total = 0
    enabled = True

    for line in data:
        matches = [match.group() for match in re.finditer(pattern, line)]
        for m in matches:
            if 'mul' in m and enabled:
                a, b = m.strip('mul()').split(',')
                total += int(a) * int(b)
            else:
                enabled = m == 'do'

    return total

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
