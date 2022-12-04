#!/usr/bin/env python3
#  https://adventofcode.com/2022/day/...


FILE = "input.txt"


def main():
    data = load_input()
    print(solve_part_1(data))
    print(solve_part_2(data))


def load_input(file=FILE) -> list:
    with open(file, "r") as f:
        return [x.strip() for x in f.readlines()]


def solve_part_1(data):
    pass


def solve_part_2(data):
    pass


if __name__ == '__main__':
    main()
