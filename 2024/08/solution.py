#!/usr/bin/env python3
# https://adventofcode.com/2024/day/8

from collections import defaultdict
from pathlib import Path
from itertools import combinations

FILE = "input.txt"
# FILE = "sample.txt"


def main():
    data = load_input()
    print(f"PART 1: {solve_part_1(data)}")
    print(f"PART 2: {solve_part_2(data)}")


def load_input(file: str = FILE) -> list:
    path = Path(__file__).with_name(file)
    with open(path, "r") as f:
        return [[l for l in line.strip()] for line in f]


def solve_part_1(data: list) -> int:
    antennas = get_antennas(data)
    max_i = len(data) - 1
    antinodes = []

    for loc in antennas.values():
        pairs = list(combinations(loc, 2))

        for a, b in pairs:
            x1, y1 = a
            x2, y2 = b

            diff = x1 - x2, y1 - y2
            ant1 = b[0] - diff[0], b[1] - diff[1]
            ant2 = a[0] + diff[0], a[1] + diff[1]

            for coord in (ant1, ant2):
                if not all((0 <= c <= max_i for c in coord)):
                    continue

                antinodes.append(coord)

    return len(set(antinodes))


def solve_part_2(data: list) -> int:
    antennas = get_antennas(data)
    max_i = len(data) - 1
    antinodes = []

    for loc in antennas.values():
        antinodes.extend(loc)
        pairs = list(combinations(loc, 2))
        
        for a, b in pairs:
            x1, y1 = a
            x2, y2 = b

            diff = x1 - x2, y1 - y2
            while True:
                coord = a[0] + diff[0], a[1] + diff[1]
                if not all((0 <= c <= max_i for c in coord)):
                    break
                antinodes.append(coord)
                a = coord

            while True:
                coord = b[0] - diff[0], b[1] - diff[1]
                if not all((0 <= c <= max_i for c in coord)):
                    break
                antinodes.append(coord)
                b = coord
    return len(set(antinodes))


def get_antennas(data: list) -> dict:
    antennas = defaultdict(list)
    for x, row in enumerate(data):
        for y, loc in enumerate(row):
            if loc != '.':
                antennas[loc].append((x, y))
    return antennas

def print_map(map: list, antinodes: list = None) -> None:
    if antinodes:
        for x, y in antinodes:
            if map[x][y] == '.':
                map[x][y] = '#'
    
    for m in map:
        print(''.join(m))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
