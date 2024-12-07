#!/usr/bin/env python3
# https://adventofcode.com/2024/day/4

from pathlib import Path

FILE = "input.txt"
FILE = "sample.txt"


def main():
    data = load_input()
    print(f"PART 1: {solve_part_1(data)}")
    print(f"PART 2: {solve_part_2(data)}")


def load_input(file: str = FILE) -> list:
    path = Path(__file__).with_name(file)
    with open(path, "r") as f:
        return [line.strip() for line in f]


def solve_part_1(data: list) -> int:
    x = 0
    count = 0
    directions = ['r', 'l', 'u', 'd', 'dl', 'dr', 'ul', 'ur']

    while x < len(data):
        y = 0
        while y < len(data[0]):
            for d in directions:
                if get_letters(x, y, data, d) == 'XMAS':
                    count += 1
            y += 1
        x += 1
    return count


def get_letters(x, y, data, direction) -> str | None:
    first = data[x][y]
    if first != 'X':
        return None
    rest = range(1, 4)
    try:
        match direction:
            case 'r':
                return first + ''.join(data[x][y+i] for i in rest)
            case 'l':
                return None if has_neg_index(y) else first + ''.join(data[x][y-i] for i in rest)
            case 'u':
                return None if has_neg_index(x) else first + ''.join(data[x-i][y] for i in rest)
            case 'd':
                return first + ''.join(data[x+i][y] for i in rest)
            case 'ur':
                return None if has_neg_index(x) else first + ''.join(data[x-i][y+i] for i in rest)
            case 'ul':
                return None if has_neg_index(y) or has_neg_index(x) else first + ''.join(data[x-i][y-i] for i in rest)
            case 'dr':
                return first + ''.join(data[x+i][y+i] for i in rest)
            case 'dl':
                    return None if has_neg_index(y) else first + ''.join(data[x+i][y-i] for i in rest)
            case _:
                return None
    except IndexError:
        return None


def has_neg_index(n) -> bool:
    for i in range(1, 4):
        if n - i < 0:
            return True
    return False

def solve_part_2(data: list) -> int:
    x = 0
    count = 0

    while x < len(data):
        y = 0
        while y < len(data[0]):
            if (to_check := get_x(x, y, data)):
                if all(c in ('MAS', 'SAM') for c in to_check):
                    count += 1
            y += 1
        x += 1
    return count


def get_x(x, y, data) -> tuple:
    mid = data[x][y]
    if mid != 'A':
        return None
    
    if (x - 1 < 0) or (y - 1 < 0):
        return None
    
    try:
        ul = data[x-1][y-1]
        ur = data[x-1][y+1]
        bl = data[x+1][y-1]
        br = data[x+1][y+1]
    except IndexError:
        return None
    
    return ul + mid + br, ur + mid + bl
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
