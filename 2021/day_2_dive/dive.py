from dataclasses import dataclass

TEST_INPUT = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

TEST_POSITION = [15, 10]
TEST_ANSWER = 150

TEST_POSITION_2 = [15, 60]
TEST_ANSWER_2 = 900


@dataclass
class Dive:
    horizontal = 0
    depth = 0
    aim = 0

    commands: dict = None
    input = 'raw_data.txt'

    def __post_init__(self):
        self.initialise_commands()

    def main(self):

        # test_text = TEST_INPUT.splitlines()
        # test_input = self.process_input_text(test_text)
        #
        # self.process_commands(test_input)
        # self.print_final_position()

        command_list = self.load_input()
        self.process_commands(command_list)
        self.print_final_position()

    def initialise_commands(self):
        self.commands = dict(
            forward=self.go_forward,
            up=self.go_up,
            down=self.go_down,
        )

    def load_input(self):
        with open(self.input, 'r') as f_in:
            text = f_in.readlines()
            return self.process_input_text(text)

    @staticmethod
    def process_input_text(text) -> list[tuple]:
        return [(cmd.split(" ")[0], int(cmd.split(" ")[1])) for cmd in text]

    def go_forward(self, distance):
        self.horizontal += distance
        self.depth += self.aim * distance

    def go_up(self, distance):
        # self.depth -= distance
        self.aim -= distance

    def go_down(self, distance):
        # self.depth += distance
        self.aim += distance

    def process_commands(self, command_input):
        for direction, value in command_input:
            cmd = self.commands.get(direction)
            print(f'{direction}({value})')
            cmd(value)
            self.print_current_position()

    def print_current_position(self):
        print(f'horizontal: {self.horizontal}, depth: {self.depth}, aim: {self.aim}')

    def print_final_position(self):
        print(f'horizontal: {self.horizontal}, depth: {self.depth}')
        print(f'Answer: {self.horizontal * self.depth}')


if __name__ == '__main__':
    app = Dive()
    app.main()
