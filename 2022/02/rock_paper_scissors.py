#!/usr/bin/env python3
#  https://adventofcode.com/2022/day/2


INPUT = "input.txt"


PART_1_SCORES = {"X": 1, "Y": 2, "Z": 3}

PART_1_RULES = {
    "A": {"X": 3, "Y": 6, "Z": 0},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"X": 6, "Y": 0, "Z": 3},
}

PART_2_SCORES = {"X": 0, "Y": 3, "Z": 6}

PART_2_RULES = {
    "A": {"X": 3, "Y": 1, "Z": 2},
    "B": {"X": 1, "Y": 2, "Z": 3},
    "C": {"X": 2, "Y": 3, "Z": 1},
}


with open(INPUT, "r") as f:
    play_list = [tuple(x.strip().split(" ")) for x in f.readlines()]


def play_game(scores: dict, rules: dict) -> int:
    return sum(
        (scores[response] + rules[play][response] for play, response in play_list)
    )


def part_1():
    score = play_game(PART_1_SCORES, PART_1_RULES)
    print(f"PART 1: {score}")


def part_2():
    score = play_game(PART_2_SCORES, PART_2_RULES)
    print(f"PART 2: {score}")


if __name__ == "__main__":
    part_1()
    part_2()
