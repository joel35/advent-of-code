# https://adventofcode.com/2021/day/6

from dataclasses import dataclass, field


def main():
    print('Part 1:')
    do_part_1()
    print('\n\nPart 2:')
    do_part_2()


def do_part_1():
    print('\nExample - 18 days')
    example = LanternfishSimPart1(
        loader=Loader('example_input'),
        hatchery=HatcheryPart1(),
        days_to_simulate=18,
        print_output=True
    )
    example.start()

    print('\nExample - 80 days')
    example = LanternfishSimPart1(
        loader=Loader('example_input'),
        hatchery=HatcheryPart1(),
        days_to_simulate=80,
        print_output=False
    )
    example.start()

    print('\nUser input - 80 days')
    app = LanternfishSimPart1(
        loader=Loader('input'),
        hatchery=HatcheryPart1(),
        days_to_simulate=80,
        print_output=False
    )
    app.start()


def do_part_2():
    print('\nExample - 256 days')
    example = LanternfishSimPart2(
        loader=Loader('example_input'),
        hatchery=HatcheryPart2(),
        days_to_simulate=256
    )
    example.start()

    print('\nUser data - 256 days')
    example = LanternfishSimPart2(
        loader=Loader('input'),
        hatchery=HatcheryPart2(),
        days_to_simulate=256
    )
    example.start()


@dataclass
class Loader:
    file: str

    def get_input(self):
        with open(self.file, 'r') as f_in:
            return f_in.read()


# Part 1
@dataclass
class HatcheryPart1:
    stock: list = field(default_factory=list)

    def make_baby(self, initial_timer=9):  # timer reduced by 1 upon creation
        self.stock.append(Fish(initial_timer, self))

    def count_fish(self):
        return len(self.stock)


@dataclass
class Fish:
    internal_timer: int
    womb: HatcheryPart1

    def age_one_day(self):
        self.internal_timer -= 1
        self.check_timer()

    def check_timer(self):
        if self.internal_timer < 0:
            self.internal_timer = 6
            self.give_birth()

    def give_birth(self):
        self.womb.make_baby()


@dataclass
class LanternfishSimPart1:
    loader: Loader
    hatchery: HatcheryPart1
    days_to_simulate: int
    print_output: bool = False
    day_timer: bool = False

    def start(self):
        data = self.loader.get_input()
        input = map(int, data.split(','))
        self.get_initial_stock(input)
        self.pass_time(self.days_to_simulate)
        total_fish = self.hatchery.count_fish()
        print(f'\tTotal fish: {total_fish}')

    def get_initial_stock(self, input):
        for i in input:
            self.hatchery.make_baby(i)

        if self.print_output:
            print(f'\tInitial state: {[fish.internal_timer for fish in self.hatchery.stock]}')

    def pass_time(self, days):
        current_day = 1

        while current_day <= days:
            [fish.age_one_day() for fish in self.hatchery.stock]
            if self.print_output:
                print(f'\tAfter {current_day} days: {[fish.internal_timer for fish in self.hatchery.stock]}')
                # print(f'After {current_day} days: {self.hatchery.count_fish()} fish')
            current_day += 1


# Part 2
@dataclass
class HatcheryPart2:
    fish_stock: dict = None

    def __post_init__(self):
        self.fish_stock = {i: 0 for i in range(9)}

    def update_stock(self):
        new_dict = {
            0: self.fish_stock[1],
            1: self.fish_stock[2],
            2: self.fish_stock[3],
            3: self.fish_stock[4],
            4: self.fish_stock[5],
            5: self.fish_stock[6],
            6: self.fish_stock[7] + self.fish_stock[0],
            7: self.fish_stock[8],
            8: self.fish_stock[0]
        }
        self.fish_stock = new_dict

    def count_fish(self):
        return sum(self.fish_stock.values())


@dataclass
class LanternfishSimPart2:
    loader: Loader
    hatchery: HatcheryPart2
    days_to_simulate: int

    def start(self):
        data = self.loader.get_input()
        input = map(int, data.split(','))
        self.get_initial_stock(input)

        for _ in range(self.days_to_simulate):
            self.add_one_day()

        print(f'\tTotal fish: {self.hatchery.count_fish()}')

    def get_initial_stock(self, input):
        for i in input:
            self.hatchery.fish_stock[i] += 1

    def add_one_day(self):
        self.hatchery.update_stock()


if __name__ == '__main__':
    main()
