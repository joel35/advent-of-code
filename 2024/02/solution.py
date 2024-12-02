#!/usr/bin/env python3
# https://adventofcode.com/2024/day/2

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
    data = [[int(level) for level in report.split()] for report in data]
    count = 0

    for line in data:
        no_dupes = list(set(line))
        asc = sorted(no_dupes) == line
        desc = sorted(no_dupes, reverse=True) == line

        if not any((asc, desc)):
            continue
        
        safe = (
            1 <= abs(line[i+1] - line[i]) <= 3
            for i
            in range(len(line)-1)
        )

        if not all(safe):
            continue

        count += 1
    
    return count


def solve_part_2(data: list) -> int:
    pass


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
