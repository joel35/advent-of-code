#!/usr/bin/env python3
# https://adventofcode.com/2023/day/5

import utils

FILE = "input.txt"
# FILE = "sample.txt"


def main():
    data = utils.load_input(FILE)
    print(f"PART 1: {solve_part_1(data)}")
    print(f"PART 2: {solve_part_2(data)}")


def solve_part_1(data: list) -> int:
    seeds = utils.get_seeds(data)
    maps = utils.get_map(data)

    locations = utils.get_locations(seeds, maps)

    return min(locations)


def solve_part_2(data: list) -> int:
    
    seeds = utils.get_seeds(data)
    maps = utils.get_map(data)
    ranges = utils.parse_seed_ranges(seeds)

    # This is returning a value +1 from what is correct
    # No idea why :(
    count = 0
    while True:
        value = count
        for map in reversed(maps):
            value = utils.get_source(map, value)
        
        for start, stop in ranges:
            if start <= value <= stop:
                if utils.get_location(value, maps) == count:
                    return count
        count += 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
