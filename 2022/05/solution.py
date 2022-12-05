#!/usr/bin/env python3
#  https://adventofcode.com/2022/day/...

import re

FILE = "input.txt"


def main():
    data = load_input()
    print(f"PART 1: {solve_part_1(data)}")
    print(f"PART 2: {solve_part_2(data)}")


def load_input(file=FILE) -> list:
    with open(file, "r") as f:
        return [line for line in f.readlines()]


def prepare_data(data) -> tuple:
    split_index = data.index('\n')

    sorted_crates = []

    for row in data[:split_index-1]:
        row = row.replace("    ", " [.] ")
        columns = [c.strip() for c in row.split(" ") if not c in ("", "\n")]
        sorted_crates.append(columns)
    
    sorted_instructions = []

    for i in [i.strip() for i in data[split_index+1:]]:
        sorted_instructions.append(tuple(int(x.strip()) for x in re.split(r'move|from|to', i) if x))

    return sorted_crates, sorted_instructions


def solve_part_1(data: tuple[list]):

    crates, instructions = data         

    pass


def solve_part_2(data):
    pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
