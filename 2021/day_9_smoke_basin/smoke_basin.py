from copy import copy

import numpy as np


def main():
    do_part_1('example_input')
    do_part_1('input')

    do_part_2('example_input')
    do_part_2('input')


def do_part_1(file):
    grid = get_grid(file)
    low_points, _ = get_low_points(grid, get_map(grid))
    print(sum(low_points, len(low_points)))


def do_part_2(file):
    grid = get_grid(file)
    _, low_point_locations = get_low_points(grid, get_map(grid))

    basins = [
        len(check_for_basin(loc[0], loc[1], grid, []))
        for loc
        in low_point_locations
    ]

    prod = np.prod(sorted(basins, reverse=True)[:3])
    print(prod)


def get_map(grid):
    rows = [r for r in range(len(grid))]
    columns = [c for c in range(len(grid[0]))]
    return [(r, c) for r in rows for c in columns]


def get_low_points(grid, map):
    low_points = []
    low_point_locations = []

    for row, column in map:
        value = grid[row][column]

        adj_values = [
            grid[loc['row']][loc['col']]
            if not not_valid(loc['row'], loc['col'], grid)
            else float('inf')
            for loc
            in get_adjacent(row, column)
        ]

        if all(value < adj_val for adj_val in adj_values):
            low_points.append(value)
            low_point_locations.append((row, column))

    return low_points, low_point_locations


def check_for_basin(row, column, grid, list):
    if not_valid(row, column, grid):
        return list

    value = copy(grid[row][column])
    grid[row][column] = -1
    adjacent = get_adjacent(row, column)

    for loc in adjacent:
        check_for_basin(loc['row'], loc['col'], grid, list)

    list.append(value)
    return list


def get_adjacent(row, column):
    top = {
        'row': row - 1,
        'col': column
    }
    bottom = {
        'row': row + 1,
        'col': column
    }
    left = {
        'row': row,
        'col': column - 1
    }
    right = {
        'row': row,
        'col': column + 1
    }

    return [top, bottom, left, right]


def not_valid(row, column, grid):
    return (row < 0 or
            row >= len(grid) or
            column < 0 or
            column >= len(grid[0]) or
            grid[row][column] == 9 or
            grid[row][column] < 0)


def get_grid(file):
    return np.array([[int(i) for i in row] for row in load_file(file).splitlines()])


def load_file(file):
    with open(file, 'r') as f_in:
        return f_in.read().strip()


if __name__ == '__main__':
    main()
