#!/usr/bin/env python3
# https://adventofcode.com/2025/day/6

from collections import defaultdict
from functools import partial, reduce
import operator
from pathlib import Path

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
    operators = {
        '+': sum,
        '*': partial(reduce, operator.mul),
    }

    data = [[l.strip() for l in line.split(' ') if l] for line in data]
    funcs = [operators[key] for key in data.pop(-1)]

    calcs = defaultdict(list)

    for row in data:
        for j, _ in enumerate(row):
            calcs[j].append(int(row[j]))

    totals = [
        funcs[i](vals) 
        for i, vals 
        in enumerate(calcs.values())
    ]
    
    return sum(totals)


def solve_part_2(data: list) -> int:
    pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
