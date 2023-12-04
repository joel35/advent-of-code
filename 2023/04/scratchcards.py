#!/usr/bin/env python3
# https://adventofcode.com/2023/day/4

from pathlib import Path
import re
from collections import deque

FILE = "input.txt"


def main():
    data = load_input()
    print(f"PART 1: {solve_part_1(data)}")
    print(f"PART 2: {solve_part_2(data)}")


def load_input(file=FILE) -> list:
    path = Path(__file__).with_name(file)
    with open(path, "r") as f:
        return [line.strip() for line in f]


def solve_part_1(data):
    return sum([get_line_score(line) for line in data])


def solve_part_2(data):
    tuple_list = create_tuples(data)
    score = 0
    to_process = deque(tuple_list)
    while to_process:
        score += 1
        index, new_lines = to_process.popleft()

        if new_lines:
            to_add = tuple_list[index : index + new_lines]
            assert len(to_add) == new_lines
            to_process.extendleft(reversed(to_add))

    return score


def get_line_score(line: str) -> int:
    _, winner_list, nums_list = parse_line(line)
    winning_nums = find_winning_numbers(winner_list, nums_list)
    score = 1 if winning_nums else 0

    if len(winning_nums) > 1:
        for _ in winning_nums[1:]:
            score *= 2

    return score


def parse_line(line: str) -> tuple[int, list, list]:
    card, winners, nums = re.split(r": | \| ", line)
    card = int(card.split()[-1])
    winner_list = winners.split()
    nums_list = nums.split()
    return card, winner_list, nums_list


def find_winning_numbers(winners: list, nums: list):
    return [n for n in nums if n in winners]


def create_tuples(data: list):
    lines = [parse_line(line) for line in data]

    return [
        (card, len(find_winning_numbers(winners, numbers)))
        for card, winners, numbers in lines
    ]


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
