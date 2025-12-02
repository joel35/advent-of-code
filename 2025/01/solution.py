#!/usr/bin/env python3
# https://adventofcode.com/2025/day/1

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
    n = 50
    total = 0

    steps = [(d[0], int(d[1:])) for d in data]

    for direction, distance in steps:
        move = -distance if direction == 'L' else distance
        n = (n + move)%100

        if n == 0:
            total += 1

    return total

def solve_part_2(data: list) -> int:
    n = 50
    total = 0

    steps = [(d[0], int(d[1:])) for d in data]

    for direction, distance in steps:
        move = -1 if direction == 'L' else 1
        for _ in range(distance):
            n = (n + move)%100           
            if n == 0:
                total += 1
    return total

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
