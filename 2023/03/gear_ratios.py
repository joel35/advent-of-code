#!/usr/bin/env python3
# https://adventofcode.com/2023/day/3

from pathlib import Path

FILE = "input.txt"


def main():
    data = load_input()
    print(f"PART 1: {solve_part_1(data)}")
    print(f"PART 2: {solve_part_2(data)}")


def load_input(file=FILE) -> list:
    path = Path(__file__).with_name(file)
    with open(path, "r") as f:
        return [list(line.strip()) for line in f]


def solve_part_1(arr):
    max_index = len(arr) - 1
    all_nums = []
    good_nums = []
    bad_nums = []
    for i, row in enumerate(arr):
        n_buffer = []
        j_buffer = []
        for j, n in enumerate(row):
            if n.isnumeric():
                n_buffer.append(n)
                j_buffer.append(j)

            if (not n.isnumeric() or j >= max_index) and n_buffer:
                num = int("".join(n_buffer))
                all_nums.append(num)

                has_symbol = check_for_symbol(row=i, columns=tuple(j_buffer), arr=arr)

                if has_symbol:
                    good_nums.append(num)
                else:
                    bad_nums.append(num)

                n_buffer, j_buffer = [], []

    assert len(good_nums) + len(bad_nums) == len(all_nums)
    return sum(good_nums)


def solve_part_2(arr):
    max_index = len(arr) - 1
    all_nums = []
    good_nums = []
    bad_nums = []
    for i, row in enumerate(arr):
        n_buffer = []
        j_buffer = []
        for j, n in enumerate(row):
            if n.isnumeric():
                n_buffer.append(n)
                j_buffer.append(j)

            if (not n.isnumeric() or j >= max_index) and n_buffer:
                num = int("".join(n_buffer))
                all_nums.append(num)

                gear_coord = check_for_symbol(
                    row=i, columns=tuple(j_buffer), arr=arr, part_2=True
                )

                if gear_coord:
                    good_nums.append({"num": num, "gear_coord": gear_coord})
                else:
                    bad_nums.append(num)

                n_buffer, j_buffer = [], []

    assert len(good_nums) + len(bad_nums) == len(all_nums)

    all_coords = [g["gear_coord"] for g in good_nums]
    good_coords = {c for c in all_coords if all_coords.count(c) > 1}

    ratios = []

    for coord in good_coords:
        nums = [g["num"] for g in good_nums if g["gear_coord"] == coord]
        assert len(nums) == 2
        ratios.append(nums[0] * nums[1])

    return sum(ratios)

def check_for_symbol(row: int, columns: tuple, arr: list, part_2=False):
    rows_to_check = [row]
    if row > 0:
        rows_to_check.append(row - 1)

    if row < len(arr) - 1:
        rows_to_check.append(row + 1)

    columns_to_check = list(columns)

    min_col, max_col = min(columns), max(columns)

    if min_col > 0:
        columns_to_check.append(min_col - 1)

    if max_col < len(arr[0]) - 1:
        columns_to_check.append(max_col + 1)

    for row in rows_to_check:
        for column in columns_to_check:
            to_check: str = arr[row][column]

            if not to_check.isnumeric():
                if part_2 and to_check == "*":
                    return (row, column)

                if not part_2 and to_check != ".":
                    return True

    return False


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
