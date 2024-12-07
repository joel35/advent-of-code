#!/usr/bin/env python3
# https://adventofcode.com/2024/day/7

from pathlib import Path
from operator import mul, add
from itertools import product

FILE = "input.txt"
# FILE = "sample.txt"


def main():
    data = load_input()
    print(f"PART 1: {solve_part_1(data)}")
    print(f"PART 2: {solve_part_2(data)}")


def load_input(file: str = FILE) -> list:
    path = Path(__file__).with_name(file)
    with open(path, "r") as f:
        data = [line.strip().split(':') for line in f]
        data = [[int(line[0]), tuple(map(int, line[-1].strip().split(' ')))]
                for line in data]
        return data


def solve_part_1(data: list) -> int:
    operators = (mul, add)
    totals = [get_good_calc(d[-1], d[0], operators) for d in data]
    return sum(totals)


def solve_part_2(data: list) -> int:
    operators = (mul, add, concat)
    totals = [get_good_calc(d[-1], d[0], operators) for d in data]
    return sum(totals)


def get_good_calc(nums, total, operators) -> int:
    ops_list = product(operators, repeat=len(nums)-1)
    for ops in ops_list:
        t = nums[0]
        for i, op in enumerate(ops):
            t = op(t, nums[i+1])
        if t == total:
            return total
    return 0


def concat(x, y) -> int:
    return int(str(x) + str(y))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
