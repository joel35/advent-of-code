#!/usr/bin/env python3
#  https://adventofcode.com/2022/day/06


FILE = "input.txt"


def main():
    data = load_input()
    print(f"PART 1: {solve_part_1(data)}")
    print(f"PART 2: {solve_part_2(data)}")


def load_input(file=FILE) -> str:
    with open(file, "r") as f:
        return f.read().strip()


def solve_part_1(data):
    return find_unique(data, 4)


def solve_part_2(data):
    return find_unique(data, 14)


def find_unique(chars: str, size: int) -> int:
    for i, _ in enumerate(chars):
        if len(set(chars[i:i + size])) == size:
            return i + size


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
