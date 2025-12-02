#!/usr/bin/env python3
# https://adventofcode.com/2025/day/2

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
    line = data[0]
    ids = [x for x in line.split(",")]
    ids = [x.split("-") for x in ids]

    bad = []

    for start, stop in ids:
        for i in range(int(start), int(stop) + 1):
            id = str(i)
            if len(id) % 2:
                continue
            middle = len(id) // 2
            if id[:middle] == id[middle:]:
                bad.append(i)
            
    return sum(bad)


def solve_part_2(data: list) -> int:
    pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
