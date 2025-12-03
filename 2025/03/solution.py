#!/usr/bin/env python3
# https://adventofcode.com/...

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
    maxes = []
    
    for line in data:
        max = 0

        for i, val_1 in enumerate(line):
            for val_2 in line[i+1:]:
                val = int(''.join(val_1 + val_2))
                if val > max:
                    max = val
        maxes.append(max)
    
    return sum(maxes)


def solve_part_2(data: list) -> int:
    maxes = []
    
    for line in data:
        drops = len(line) - 12
        stack = []

        for num in line:
            while stack and drops > 0 and stack[-1] < num:
                stack.pop()
                drops -= 1
            stack.append(num)
        
        maxes.append(int(''.join(stack[:12])))

    return sum(maxes)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
