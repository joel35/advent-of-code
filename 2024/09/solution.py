#!/usr/bin/env python3
# https://adventofcode.com/2024/day/9

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
        data = [line.strip() for line in f]
        data = list(map(int, data[0]))
        return data


def solve_part_1(data: list) -> int:
    disc_map = parse_data(data)

    i, j = 0, len(disc_map) - 1
    while i < j:
        if not disc_map[i] == ".":
            i += 1
            continue
        if not (block := disc_map.pop(j)) == ".":
            disc_map[i] = block
            i += 1
        j -= 1

    return get_checksum(disc_map)


def solve_part_2(data: list) -> int:
    disc_map = parse_data(data)
    gap_map = get_gap_map(disc_map)

    i = len(disc_map) - 1
    j = len(disc_map) - 2

    while i > 0:
        block = disc_map[i]
        if block == ".":
            i -= 1
            continue

        stack = [block]
        j = i - 1
        while (new := disc_map[j]) == block:
            stack.append(new)
            j -= 1

        window = len(stack)

        for start_i in sorted(gap_map.keys()):
            if start_i > j:
                break
            if gap_map[start_i] < window:
                continue

            disc_map[start_i : start_i + window] = stack
            disc_map[j + 1 : i + 1] = ("." for _ in stack)

            remaining = gap_map.pop(start_i) - window
            if remaining:
                new_i = start_i + window
                gap_map[new_i] = remaining
            break

        i = j
        continue

    return get_checksum(disc_map)


def parse_data(data: list) -> list:
    result = []
    j = 0
    for i, x in enumerate(data):
        if i == 0:
            char = 0
        elif i % 2 == 0:
            j += 1
            char = j
        else:
            char = "."
        for _ in range(x):
            result.append(char)
    return result


def get_checksum(data: list) -> int:
    return sum((i * d for i, d in enumerate(data) if isinstance(d, int)))


def get_gap_map(data: list) -> dict:
    gap_map = {}

    i = 0
    j = 1
    while i < len(data):
        check = data[i]
        if not check == ".":
            i += 1
            continue

        j = i + 1
        while j < len(data):
            if not data[j] == check:
                gap_map[i] = j - i
                break
            j += 1

        i = j
    return gap_map


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
