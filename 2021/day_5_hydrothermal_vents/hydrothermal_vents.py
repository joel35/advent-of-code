from dataclasses import dataclass
import numpy as np


def main():
    print('Example')
    example = HydrothermalVents(
        loader=Loader('example_input'),
        grid_util=Grid(),
        coord_util=Coordinates()
    )
    example.start()

    print('My input')
    app = HydrothermalVents(
        loader=Loader('input'),
        grid_util=Grid(),
        coord_util=Coordinates()
    )
    app.start()


@dataclass
class Loader:
    file: str

    def get_input(self):
        with open(self.file, 'r') as f_in:
            return f_in.read()


@dataclass
class Grid:
    grid: np.ndarray = None

    def get_grid(self, index):
        self.grid = np.zeros((index, index), dtype=int)
        return self.grid

    def add_values_to_grid(self, coords, value=1):
        for row, column in coords:
            self.grid[row][column] += value
        return self.grid

    def count_grid_vals(self, number):
        return np.sum(self.grid >= number)


@dataclass
class Coordinates:
    coords: list = None
    max_index: int = -1

    def get_coords(self, input):
        dirty = input.strip().splitlines()

        self.coords = []
        for group in dirty:
            coord = [tuple([int(i) for i in val.split(',')])
                     for val
                     in group.split(' -> ')]
            self.coords.append(coord)

        self.max_index = self.get_max_index(self.coords)
        return self.coords

    def get_coord_tuple(self, x1, x2, y1, y2) -> list:
        x_range = self.get_range(x1, x2)
        y_range = self.get_range(y1, y2)
        x_range, y_range = self.match_range_lens(x_range, y_range)
        return [i for i in zip(y_range, x_range)]

    @staticmethod
    def get_range(from_val, to_val) -> list[int]:
        return [i for i in range(from_val, to_val - 1, -1)] if from_val > to_val else [i for i in
                                                                                       range(from_val, to_val + 1)]

    @staticmethod
    def match_range_lens(range_1, range_2):
        if len(range_1) == 1:
            range_1 = range_1 * len(range_2)

        if len(range_2) == 1:
            range_2 = range_2 * len(range_1)

        return range_1, range_2

    @staticmethod
    def get_max_index(coords):
        return np.max(coords) + 1


@dataclass
class HydrothermalVents:
    loader: Loader
    grid_util: Grid
    coord_util: Coordinates

    def start(self):
        input = self.loader.get_input()
        self.coord_util.get_coords(input)

        self.do_part_1()
        self.do_part_2()

    def do_part_1(self):
        self.grid_util.get_grid(self.coord_util.max_index)
        print(self.check_coordinates(part=1))
        print(f'Two or more overlaps: {self.grid_util.count_grid_vals(2)}')

    def do_part_2(self):
        self.grid_util.get_grid(self.coord_util.max_index)
        print(self.check_coordinates(part=2))
        print(f'Two or more overlaps: {self.grid_util.count_grid_vals(2)}')

    def check_coordinates(self, part: int = None):
        print(f'part: {part}')
        for (x1, y1), (x2, y2) in self.coord_util.coords:
            if part == 1 and not any([x1 == x2, y1 == y2]):
                continue

            coord_tuple = self.coord_util.get_coord_tuple(x1, x2, y1, y2)
            self.grid_util.add_values_to_grid(coord_tuple)

        return self.grid_util.grid


if __name__ == '__main__':
    main()
