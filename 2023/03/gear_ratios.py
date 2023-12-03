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
        return [line.strip() for line in f]


def solve_part_1(data):
    arr = parse_data(data)
    nums = []
    good_nums = []
    symbols = []
    # arr = arr[-2:]
    for i, row in enumerate(arr):
        n_buffer = []
        j_buffer = []
        for j, n in enumerate(row):
            if n.isnumeric():
                n_buffer.append(n)
                j_buffer.append(j)
                continue

            if not n.isnumeric() and len(n_buffer) > 0:

                n_row = i

                nums.append({
                    'num': int(''.join(n_buffer)),
                    'row': n_row,
                    'columns': tuple(j_buffer)
                    })
                n_buffer = []
                j_buffer = []
            
            if n == '.':
                continue
            
            symbols.append((i, j))

    # print(f'{nums=}')
    # print(f'{symbols=}')

    for num in nums:
        # print(num)
        row = num['row']
        rows_to_check = [row]
        if row > 0:
            rows_to_check.append(row - 1)
        
        if row < len(arr) - 1:
            rows_to_check.append(row + 1)

        # print(rows_to_check)

        columns = num['columns']
        # print(columns)

        columns_to_check = list(columns)

        if columns[0] > 0:
            columns_to_check.append(columns[0] - 1)
        
        if columns[-1] < len(arr[0]) - 1:
            columns_to_check.append(columns[-1] + 1)
        
        # print(columns_to_check)

        for r, c in symbols:
            # print(r, c)
            # print(r in rows_to_check, c in columns_to_check)
            if r in rows_to_check and c in columns_to_check:
                good_nums.append(num['num'])
                break
    
    # print(good_nums)
    return sum(good_nums)


def solve_part_2(data):
    pass

def parse_data(data: list[str]) -> list[list[str]]:
    return [list(d) for d in data]

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
