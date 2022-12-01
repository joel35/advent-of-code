# https://adventofcode.com/2021/day/4
import copy
from dataclasses import dataclass
import numpy as np


@dataclass
class GiantSquid:
    file: str
    numbers: list = None
    boards: list = None

    def __call__(self, *args, **kwargs):
        return self.main()

    def main(self):
        input = self.load_input_file(self.file).splitlines()
        input = self.clean_list(input)
        self.numbers = self.get_numbers(input.pop(0))
        self.boards = self.get_boards(input)

        self.do_part_1()
        self.do_part_2()

    def do_part_1(self):
        _, winner, number = self.get_winner(self.numbers, self.boards)
        print('Part One')
        print(f'Board {winner.id} is a winner!')
        print(f'Score: {winner.score}. Number: {number}')
        print(f'Final score: {winner.score * number}')

    def do_part_2(self):
        loser, number = self.find_last_winner(copy.deepcopy(self.boards))
        print('Part Two')
        print(f'Board {loser.id} is the loser!')
        print(f'Score: {loser.score}. Number: {number}')
        print(f'Final score: {loser.score * number}')

    def find_last_winner(self, boards):
        i, board, number = self.get_winner(self.numbers, boards)

        if len(boards) == 1:
            return boards[0], number

        boards.pop(i)
        return self.find_last_winner(boards)

    @staticmethod
    def get_winner(numbers, boards):
        for number in numbers:
            for i, board in enumerate(boards):
                if board is not None and board.check_board(number):
                    return i, board, number
        return None

    @staticmethod
    def clean_list(lst):
        return [i for i in lst if i != '']

    @staticmethod
    def get_numbers(input):
        numbers = input.strip().split(',')
        return [int(i) for i in numbers]

    @staticmethod
    def load_input_file(file):
        with open(file, 'r') as f_in:
            return f_in.read()

    @staticmethod
    def get_boards(lst):
        boards = [lst[i:i + 5] for i in range(0, len(lst), 5)]
        return [Board(i, board) for i, board in enumerate(boards, start=1)]


class Board:

    def __init__(self, ident: int, array: list):
        self.id = ident
        self.board = self.prepare_board(array)
        self.score = None

    @staticmethod
    def prepare_board(array: list) -> np.ndarray:
        temp_array = []

        for row in array:
            row = [int(num) for num in row.split(' ') if num != '']
            temp_array.append(row)

        return np.array(temp_array)

    def check_board(self, number: int) -> bool:
        row, column = np.where(self.board == number)
        if row.size > 0 and column.size > 0:
            self.board[row, column] = -1
        return self.is_winner()

    def is_winner(self) -> bool:
        row_totals = np.sum(self.board, axis=0)
        column_totals = np.sum(self.board, axis=1)

        if -5 in row_totals or -5 in column_totals:
            self.score = self.check_score()
            return True
        return False

    def check_score(self) -> int:
        remaining = self.board[self.board > -1]
        return int(np.sum(remaining))


if __name__ == '__main__':
    print('***EXAMPLE***')
    example = GiantSquid('example.txt')
    example()
    print()

    print('***REAL***')
    squid = GiantSquid('input.txt')
    squid()
