#!/usr/bin/env python3
# https://adventofcode.com/2024/day/6

from collections import deque
from functools import partial
from pathlib import Path
from copy import deepcopy
from concurrent.futures import ProcessPoolExecutor

FILE = "input.txt"
# FILE = "sample.txt"

DIRECTIONS = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0,),
    '<': (0, -1)
}

def main():
    data = load_input()
    print(f"PART 1: {solve_part_1(deepcopy(data))}")
    print(f"PART 2: {solve_part_2(deepcopy(data))}")


def load_input(file: str = FILE) -> list:
    path = Path(__file__).with_name(file)
    with open(path, "r") as f:
        return [[x for x in line.strip()] for line in f]


def solve_part_1(data: list) -> int:
    guards = deque(('^', '>', 'v', '<'))
    x, y = find_guard(data, guards)
    coords = get_item_coords(data, '#')
    path = plot_path(coords, x, y, guards, len(data))
    return len(set(path))

# Can't get this to run quickly enough to actually finish :(
def solve_part_2(data: list) -> int:
    guards = deque(('^', '>', 'v', '<'))
    x, y = find_guard(data, guards)
    barriers = get_item_coords(data, '#')
    path = plot_path(barriers, x, y, guards, len(data))
    custom_barriers = get_custom_barriers(data, path)
    print(len(custom_barriers))

    check_loop = partial(
        plot_path_custom_loops, 
        barriers=barriers,
        x=x,
        y=y,
        guards=deque(('^', '>', 'v', '<')),
        max_i=len(data)
    )

    with ProcessPoolExecutor() as ex:
        loops = ex.map(check_loop, custom_barriers)
    

    return len([l for l in loops if l])


def find_guard(data, guards) -> tuple:
    for x, row in enumerate(data):
        for y, spot in enumerate(row):
            if spot in guards:
                return x, y


def plot_path(barriers: list, x: int, y: int, guards: deque, max_i: int) -> list:
    path = []
    while 0 <= x <= max_i and 0 <= y <= max_i:
        guard = guards[0]
        add_x, add_y = DIRECTIONS[guard]

        new_x = x + add_x
        new_y = y + add_y

        if (new_x > max_i) or (new_y > max_i):
            break

        if (new_x, new_y) in barriers:
            guards.rotate(-1)
            continue

        path.append((x, y))
        x = new_x
        y = new_y

    return path


def plot_path_custom_loops(custom_barrier: tuple, barriers: list, x: int, y: int, guards: deque, max_i: int) -> list:
    history = []

    while True:
        guard = guards[0]
        add_x, add_y = DIRECTIONS[guard]

        position = x, y
        new_position = x + add_x, y + add_y

        if not all(0 <= p <= max_i for p in new_position):
            break

        if new_position in barriers + [custom_barrier]:
            guards.rotate(-1)
            continue

        if (new_position, guard) in history:
            return True

        history.append((position, guard))
        x, y = new_position

    return False


def get_item_coords(data: list, item: str) -> list:
    coords = []

    for x in range(len(data)):
        for y in range(len(data[0])):
            if data[x][y] == item:
                coords.append((x, y))
    return coords


def get_custom_barriers(data: list, guard_path: list) -> list:

    barriers = []

    for x in range(len(data)):
        for y in range(len(data[0])):
            if data[x][y] in '#^<>v':
                continue
            if (x, y) not in guard_path:
                continue
            barriers.append((x, y))
    return barriers

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
