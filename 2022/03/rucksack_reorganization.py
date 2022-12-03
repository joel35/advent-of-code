#!/usr/bin/env python3
#  https://adventofcode.com/2022/day/3

import string

FILE = "input.txt"


def main():
    data = load_input()
    print(f"PART 1: {solve_part_1(data)}")
    print(f"PART 2: {solve_part_2(data)}")


def load_input():
    with open(FILE, "r") as f:
        return [x.strip() for x in f.readlines()]


def solve_part_1(data: list):
    matching = [p1_find_matching(item) for item in data]
    scores = [get_score(letter) for letter in matching]
    return sum(scores)


def solve_part_2(data: list) -> int:
    groups = p2_get_groups(data)
    matching = [p2_find_matching(group) for group in groups]
    scores = [get_score(letter) for letter in matching]
    return sum(scores)


def p1_find_matching(sack: str) -> str:
    half = int(len(sack) / 2)
    for x in sack[:half]:
        if x in sack[half:]:
            return x


def p2_get_groups(data: list) -> list[tuple]:
    return [tuple(data[i:i + 3]) for i in range(0, len(data), 3)]


def p2_find_matching(group: tuple) -> str:
    group_list = [list(iter(g)) for g in group]
    unique = list(set(group_list[0]) & set(group_list[1]) & set(group_list[2]))
    return unique[0]


def get_score(letter: str) -> int:
    offset = {c: 96 for c in string.ascii_lowercase}
    offset.update({c: 38 for c in string.ascii_uppercase})
    return ord(letter) - offset[letter]


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
