#!/usr/bin/env python3
#  https://adventofcode.com/2022/day/4


FILE = "input.txt"


def main():
    data = prepare_data(load_input())
    print(solve_part_1(data))
    print(solve_part_2(data))


def load_input():
    with open(FILE, "r") as f:
        return [x.strip() for x in f.readlines()]


def solve_part_1(data):
    return len([
        (a, b)
        for a, b
        in data
        if len(list(set(a) & set(b))) in (len(a), len(b))
    ])


def solve_part_2(data):
    return len([
        (a, b)
        for a, b
        in data
        if len(list(set(a) & set(b)))
    ])


def prepare_data(data):
    cleaned = []
    for pair in data:
        lst = []
        for c in pair.split(","):
            start, fin = c.split('-')
            lst.append(list(range(int(start), int(fin) + 1)))
        cleaned.append(tuple(lst))

    return cleaned


if __name__ == '__main__':
    main()
