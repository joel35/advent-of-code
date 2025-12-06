#!/usr/bin/env python3
# https://adventofcode.com/2025/day/6

from collections import defaultdict
from functools import partial, reduce
import operator
from pathlib import Path

FILE = "input.txt"
# FILE = "sample.txt"

OPERATORS = {
    '+': sum,
    '*': partial(reduce, operator.mul),
}

def main():
    data = load_input()
    print(f"PART 1: {solve_part_1(data)}")
    print(f"PART 2: {solve_part_2(data)}")


def load_input(file: str = FILE) -> list:
    path = Path(__file__).with_name(file)
    return path.read_text().splitlines()



def solve_part_1(data: list) -> int:
    data = [[l.strip() for l in line.split(' ') if l] for line in data]
    funcs = [OPERATORS[key] for key in data.pop(-1)]

    calcs = defaultdict(list)

    for row in data:
        for j, _ in enumerate(row):
            calcs[j].append(int(row[j]))

    totals = [
        funcs[i](vals) 
        for i, vals 
        in enumerate(calcs.values())
    ]
    
    return sum(totals)


def solve_part_2(data: list) -> int:
    digit_rows = data[:-1]
    ops_row = data[-1]

    width = max(map(len, data), default=0)

    # Normalize rows to equal width
    pad = lambda s: s.ljust(width)
    digit_rows = list(map(pad, digit_rows))
    # ops_row = pad(ops_row)

    # Column classification: does column contain any digit?
    is_digit_col = [any(row[c].isdigit() for row in digit_rows) for c in range(width)]

    # Detect contiguous spans of digit columns: [(start, end), ...]
    def spans(flags):
        spans = []
        start = None
        for idx, flag in enumerate(flags + [False]):  # sentinel to flush last
            if flag and start is None:
                start = idx
            elif not flag and start is not None:
                spans.append((start, idx))
                start = None
        return spans

    blocks = spans(is_digit_col)

    # Build numbers per block: left-to-right columns, vertical digits only
    def col_number(c):
        vchars = (row[c] for row in digit_rows)
        digits = ''.join(ch for ch in vchars if ch.isdigit())
        return int(digits) if digits else None

    def block_numbers(start_end):
        s, e = start_end
        nums = list(filter(lambda x: x is not None, (col_number(c) for c in range(s, e))))
        return nums
    
    def get_func(ops_row, span):
        key = ops_row[span[0]:span[1]].strip()
        return OPERATORS[key]

    totals = (
        get_func(ops_row, span)(block_numbers(span))
        for span in blocks
    )

    return sum(totals)


ret = {
    0: ([356, 24, 1], '*'),
    1: ([8, 248, 369], '+'),
    2: ([175, 581, 32], '*'),
    3: ([4, 431, 623], '+')
}




if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
