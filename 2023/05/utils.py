import re
from pathlib import Path


def load_input(file: str) -> list:
    path = Path(__file__).with_name(file)
    with open(path, "r") as f:
        return [line for line in f]


def get_seeds(data: list) -> list:
    return [
        int(seed)
        for seed_string in data
        if "seeds: " in seed_string
        for seed in seed_string.strip().split()[1:]
    ]


def parse_map(map: list) -> list:
    key = re.split(r"-to-| ", map[0].strip())[:2]
    parsed = []
    # print(key)

    for vals in map[1:]:
        dest, source, num = [int(v) for v in vals.strip().split()]
        parsed.append([dest, source, num])

    return parsed

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


def get_destination(map: list, source: int) -> int:
    for m in map:
        dest_start, source_start, steps = m

        if source_start <= source <= source_start + steps:
            i = source - source_start
            return dest_start + i
    return source

def get_source(map: list, destination: int) -> int:
    for m in map:
        dest_start, source_start, steps = m

        if dest_start <= destination <= (dest_start + steps):
            i = destination - dest_start
            return source_start + i
    return destination


def get_location(value: int, maps: list) -> int:
    for map in maps:
        value = get_destination(map, value)
    return value

def get_locations(seeds: list, maps: list):
    locations = []

    for value in seeds:
        get_location(value, maps)
        locations.append(value)
    
    return locations

def parse_seed_ranges(ranges: list) -> list[tuple]:
    i = 0
    r = []

    while i <= len(ranges)-1:
        r_start = ranges[i]
        r_stop = ranges[i] + ranges[i+1]
        r.append((r_start, r_stop))
        i += 2
    
    return r

def find_lowest_location(seeds: list, maps) -> int:
    lowest = float('inf')
    for seed in seeds:
        location = get_location(seed, maps)
        
        # print(f'{seed=}, {location=}')
        if location < lowest:
            lowest = location
    return lowest