#!/usr/bin/env python3
# https://adventofcode.com/2023/day/6

import dis
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
    data = [tuple(int(i) for i in line.split()[1:]) for line in data]

    product = 1

    for time, distance in zip(data[0], data[-1]):
        product *= count_wins(time, distance)

    return product


def solve_part_2(data: list) -> int:
    data = (tuple(i for i in line.split()[1:]) for line in data)
    time, distance = tuple(int(''.join(x)) for x in data)
    return count_wins(time, distance)


def count_wins(time: int, distance: int) -> int:
    count = 0
    for i in range(time):
        if i * (time - i) > distance :
            count += 1
    return count


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
