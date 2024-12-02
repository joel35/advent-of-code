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
    return [is_safe(line) for line in data].count(True)


def solve_part_2(data: list) -> int:
    data = [[int(level) for level in report.split()] for report in data]
    safe_list = []
    for line in data:
        if is_safe(line):
            safe_list.append(line)
            continue
        
        for i in range(len(line)):
            if is_safe(line[:i] + line[i+1:]):
                safe_list.append(line)
                break
    
    return len(safe_list)

def is_safe(line: list) -> bool:
    asc = []
    desc = []
    diff = []
    
    for i in range(len(line) - 1):
        asc.append(line[i] < line[i+1])
        desc.append(line[i] > line[i+1])
        diff.append(1 <= abs(line[i] - line[i+1]) <= 3)
    
    return (all(asc) or all(desc)) and all(diff)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
