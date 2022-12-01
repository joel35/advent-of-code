from abc import ABC
from dataclasses import dataclass
from functools import cache


def main():
    do_part_1()
    do_part_2()


def do_part_1():
    example = TreacheryOfWhales(loader=Loader('example_input'), solver=Part1())
    print(f'Part 1 example passes: {example.start() == 37}')

    part_1 = TreacheryOfWhales(loader=Loader('input'), solver=Part1())
    part_1.start()


def do_part_2():
    example = TreacheryOfWhales(loader=Loader('example_input'), solver=Part2())
    print(f'Part 2 example passes: {example.start() == 168}')

    part_2 = TreacheryOfWhales(loader=Loader('input'), solver=Part2())
    part_2.start()


@dataclass
class Loader:
    file: str

    def __call__(self):
        with open(self.file, 'r') as f_in:
            return self.clean_input(f_in.read())

    @staticmethod
    def clean_input(input):
        return [int(i) for i in input.split(',')]


class Solver(ABC):
    best_location = None
    least_fuel = float('inf')

    def __call__(self, input):
        for loc in range(max(input)):
            fuel_needed = self.get_total_fuel_needed(input, loc)
            self.update_best_stats(fuel_needed, loc)

        self.print_solution()
        return self.least_fuel

    def update_best_stats(self, fuel, location):
        if fuel < self.least_fuel:
            self.least_fuel = fuel
            self.best_location = location

    def get_total_fuel_needed(self, crabs, target):
        return sum([self.get_crab_fuel(abs(crab - target)) for crab in crabs])

    def get_crab_fuel(self, places_to_move):
        return places_to_move

    def print_solution(self):
        print(f'Best position: {self.best_location}, Fuel: {self.least_fuel}')


class Part1(Solver):
    pass


class Part2(Solver):
    @cache
    def get_crab_fuel(self, places_to_move):
        return sum(range(1, places_to_move + 1, 1))


@dataclass
class TreacheryOfWhales:
    loader: Loader
    solver: Solver

    def start(self):
        return self.solver(self.loader())


if __name__ == '__main__':
    main()
