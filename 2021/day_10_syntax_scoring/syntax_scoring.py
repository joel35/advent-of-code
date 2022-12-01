import math
from abc import ABC, abstractmethod
from collections import deque
from dataclasses import dataclass


def main():
    load = Loader()
    print(f"Part 1 answer: {Part1()(load('input'))}")
    print(f"Part 2 answer: {Part2()(load('input'))}")


class Solver(ABC):
    chunks = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    @abstractmethod
    def __call__(self, input):
        pass

    def get_illegal(self, line):
        stack = deque()
        for i, char in enumerate(line):
            if char in self.chunks.keys():
                stack.append(char)
            elif char == self.chunks[stack[-1]]:
                stack.pop()
            else:
                return char


class Part1(Solver):
    scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    def __call__(self, input):
        illegals = [self.get_illegal(line) for line in input]
        return self.get_score(illegals)

    def get_score(self, illegals):
        return sum(self.scores[char] for char in illegals if char is not None)


class Part2(Solver):
    scores = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }

    def __call__(self, input):
        incomplete = [line for line in input if self.get_illegal(line) is None]
        closers = [self.get_closers(line) for line in incomplete]
        scores = [self.get_score(closer) for closer in closers]
        return self.get_middle_score(scores)

    def get_closers(self, line):
        stack = deque()

        for i, char in enumerate(line):
            if char in self.chunks.keys():
                stack.append(char)
            elif char == self.chunks[stack[-1]]:
                stack.pop()
            else:
                continue

        return ''.join(self.chunks[o] for o in reversed(stack))

    def get_score(self, line):
        score = 0

        for char in line:
            score *= 5
            score += self.scores[char]

        return score

    @staticmethod
    def get_middle_score(scores: list):
        i = int(len(scores) / 2)
        return sorted(scores)[i]


class Loader:
    def __call__(self, file: str):
        return self.clean_data(self.load_file(file))

    @staticmethod
    def load_file(file: str):
        with open(file, 'r') as f_in:
            return f_in.read().strip()

    @staticmethod
    def clean_data(data: str):
        return data.splitlines()


if __name__ == '__main__':
    main()
