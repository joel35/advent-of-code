#!/usr/bin/env python3
# https://adventofcode.com/2025/day/5

from collections import Counter
from pathlib import Path

FILE = "input.txt"
# FILE = "sample.txt"


def main():
    data = load_input()
    print(f"PART 1: {solve_part_1(*data)}")
    print(f"PART 2: {solve_part_2(data[0])}")


def load_input(file: str = FILE) -> tuple:
    path = Path(__file__).with_name(file)
    with open(path, "r") as f:
        lines = [line.strip() for line in f]
        split_idx = lines.index("")
        ranges = [tuple(map(int, r.split("-"))) for r in lines[:split_idx]]
        data = [int(d) for d in lines[split_idx + 1 :]]
        return ranges, data


def solve_part_1(ranges: list, data: list) -> int:
    ranges = [range(r[0], r[1] + 1) for r in ranges]
    data = [d for d in data if any(d in r for r in ranges)]
    return len(data)


def solve_part_2(ranges: list) -> int:
    ranges = sorted(ranges, key=lambda x: x[0])
    start, end = ranges.pop(0)
    merged = []

    for r_start, r_end in ranges:
        if r_start <= end + 1:
            end = max(end, r_end)
        else:
            merged.append(range(start, end + 1))
            start, end = r_start, r_end

    merged.append(range(start, end + 1))
    return sum(len(r) for r in merged)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
