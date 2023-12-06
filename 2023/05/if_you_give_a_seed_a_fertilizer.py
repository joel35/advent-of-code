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
    maps = get_map(data)
    # print(seeds)
    # print(maps)
    destinations = []

    sample_destinations = [82, 43, 86, 35]

    for seed, sample in zip(seeds, sample_destinations):
        history = [seed]
        mapped_num = seed
        for map in maps:
            for dest, source, num in map:
                if source <= mapped_num <= source + num:
                    # print(f'{min_n} <= {mapped_num} <= {max_n}')
                    # print(f'{dest=} {source=} {num=}')
                    diff = mapped_num - source
                    # print(f'{mapped_num}-{min_n}={diff}')
                    mapped_num = dest + diff
                    # print(f'{dest}+{diff}={mapped_num}')
                    # print()

            history.append(mapped_num)
        print(f'{mapped_num}={sample}: {mapped_num==sample}; {history}')
        destinations.append(mapped_num)
        # print(history)
    # print(destinations)
    return min(destinations)


def get_seeds(data: list) -> list:
    return [
        int(seed)
        for seed_string in data
        if "seeds: " in seed_string
        for seed in seed_string.strip().split()[1:]
    ]


def get_map(data: list):
    gap_indices = [i + 1 for i, _ in enumerate(data) if _ == "\n"]

    if (last_index := len(data) + 1) not in gap_indices:
        gap_indices.append(last_index)

    maps = [
        data[gap_indices[i - 1] : gap_indices[i] - 1]
        for i in range(1, len(gap_indices))
    ]

    parsed_maps = [parse_map(map) for map in maps]

    return parsed_maps


def parse_map(map: list) -> list:
    key = re.split(r"-to-| ", map[0].strip())[:2]
    parsed = []
    # print(key)

    for vals in map[1:]:
        dest, source, num = [int(v) for v in vals.strip().split()]
        parsed.append([dest, source, num])

    return parsed


def solve_part_2(data):
    pass


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
