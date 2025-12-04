#!/usr/bin/env python3
# https://adventofcode.com/...

from pathlib import Path

FILE = "input.txt"
# FILE = "sample.txt"


def main():
    data = load_input()
    print(f"PART 1: {solve_part_1(data.copy())}")
    print(f"PART 2: {solve_part_2(data.copy())}")


def load_input(file: str = FILE) -> list:
    path = Path(__file__).with_name(file)
    with open(path, "r") as f:
        return [list(line.strip()) for line in f]


def solve_part_1(data: list) -> int: 
    total = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != '@':
                continue
            neighbors = get_neighours(i, j, data)
            count = sum(neighbor == '@' for neighbor in neighbors)
            if count < 4:
                total += 1

    return total


def solve_part_2(data: list) -> int:
    total = 0

    for _ in range(1000):
        starting_total = total

        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] != '@':
                    continue
                neighbors = get_neighours(i, j, data)
                count = sum(neighbor == '@' for neighbor in neighbors)
                if count < 4:
                    total += 1
                    data[i][j] = '.'
        
        if total == starting_total:
            break

    return total

def get_neighours(i: int, j: int, data: list) -> list:
    neighbors = []
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            ni, nj = i + di, j + dj
            if (di != 0 or dj != 0) and 0 <= ni < len(data) and 0 <= nj < len(data[i]):
                neighbors.append(data[ni][nj])
    return neighbors

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
