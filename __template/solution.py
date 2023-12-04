#!/usr/bin/env python3
# https://adventofcode.com/...

from pathlib import Path

FILE = "input.txt"


def main():
    data = load_input()
    print(f"PART 1: {solve_part_1(data)}")
    print(f"PART 2: {solve_part_2(data)}")


def load_input(file=FILE) -> list:
    path = Path(__file__).with_name(file)
    with open(path, "r") as f:
        return [line.strip() for line in f]


def solve_part_1(data):
    pass


def solve_part_2(data):
    pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
