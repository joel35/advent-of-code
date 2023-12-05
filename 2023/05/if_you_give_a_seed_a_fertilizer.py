#!/usr/bin/env python3
# https://adventofcode.com/2023/day/5

from pathlib import Path
import re

FILE = "sample.txt"


def main():
    data = load_input()
    print(f"PART 1: {solve_part_1(data)}")
    print(f"PART 2: {solve_part_2(data)}")


def load_input(file=FILE) -> list:
    path = Path(__file__).with_name(file)
    with open(path, "r") as f:
        return [line for line in f]


def solve_part_1(data):
    seeds = get_seeds(data)
    print(seeds)
    map = get_map(data)


def get_seeds(data: list) -> list:
    return [
        int(seed)
        for seed_string in data
        if "seeds: " in seed_string
        for seed in seed_string.strip().split()[1:]
    ]


def get_map(data: list):
    gap_indices = [i + 1 for i, _ in enumerate(data) if _ == "\n"]

    maps = [
        data[gap_indices[i - 1] : gap_indices[i] - 1]
        for i in range(1, len(gap_indices))
    ]

    # print(maps)

    map = maps[0]
    print(map)

    key = re.split(r'-to-| ', map[0].strip())[:2]
    print(key)

    source_list = []
    dest_list = []

    for vals in map[1:]:
        destination, source, num = [int(v) for v in vals.strip().split()]

        print(source, destination, num)

        for s in range(source, source+num):
            source_list.append(s)
        
        for n in range(max(source_list)):
            if n not in source_list:
                source_list.append(n)
        
        for d in range(destination, destination + num):
            dest_list.append(d)
        
        for n in range(max(dest_list)):
            if n not in dest_list:
                dest_list.append(n)
        
    
    zipped = {s: d for s, d in zip(source_list, dest_list)}
    print(zipped)

    


def solve_part_2(data):
    pass


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
