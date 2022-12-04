#!/usr/bin/env python3
#  https://adventofcode.com/2022/day/...


FILE = "input.txt"


def main():
    data = load_input()
    print(f"PART 1: {solve_part_1(data)}")
    print(f"PART 2: {solve_part_2(data)}")


def load_input(file=FILE) -> list:
    with open(file, "r") as f:
        return [line.strip() for line in f.readlines()]


def solve_part_1(data):
    pass


def solve_part_2(data):
    pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
