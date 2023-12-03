#!/usr/bin/env python3
#  https://adventofcode.com/2023/day/2


import re
from pathlib import Path


FILE = "input.txt"


def main():
    data = load_input()
    print(f"PART 1: {solve_part_1(data)}")
    print(f"PART 2: {solve_part_2(data)}")


def load_input(file=FILE) -> list:
    path = Path(__file__).with_name(file)
    print(f'{path=}')
    with open(path) as f:
        return [line.strip() for line in f]


def solve_part_1(data):
    maxes = {"red": 12, "green": 13, "blue": 14}
    possible = []

    for line in data:
        game, colours = prepare_line(line)
        is_possible = True

        for n, colour in colours:
            if n > maxes[colour]:
                is_possible = False
                break

        if is_possible:
            possible.append(game)

    return sum(possible)


def solve_part_2(data):
    powers = []

    for line in data:
        maxes = {"red": 0, "green": 0, "blue": 0}
        _, colours = prepare_line(line)

        for n, colour in colours:
            if n > maxes[colour]:
                maxes[colour] = n

        red, green, blue = maxes.values()
        powers.append(red * green * blue)
    return sum(powers)


def prepare_line(line: str) -> tuple[int, list]:
    cleaned = re.split(f", |; |: ", line)
    game = int(cleaned[0].split()[-1])
    pairs = []

    for pair in cleaned[1:]:
        count, colour = pair.split()
        pairs.append((int(count), colour))

    return game, pairs


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
