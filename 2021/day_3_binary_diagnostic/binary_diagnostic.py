# https://adventofcode.com/2021/day/3
from collections import Counter
from dataclasses import dataclass


@dataclass
class Example:
    input = """00100
    11110
    10110
    10111
    10101
    01111
    00111
    11100
    10000
    11001
    00010
    01010"""

    most_common = [1, 0, 1, 1, 0]
    gamma_rate_binary = 0b10110
    gamma_rate_decimal = 22

    epsilon_rate_binary = 0b01001
    epsilon_rate_decimal = 9
    power_consumption = 198

    oxygen_generator_default = 1
    oxygen_generator_binary = 0b10111
    oxygen_generator_decimal = 23

    c02_scrubber_default = 0
    c02_scrubber_binary = 0b01010
    c02_scrubber_decimal = 10

    life_support_rating = 230


@dataclass
class BinaryDiagnostic:
    file = 'input.txt'
    in_data = None

    def main(self):
        self.in_data = self.load_file(self.file)
        # self.in_data = Example.input
        processed_input = self.process_input(self.in_data)

        self.do_part_1(processed_input)
        self.do_part_2(processed_input)

    def do_part_1(self, data):
        most_common = self.get_most_common(data)
        least_common = self.get_least_common(data)
        gamma_rate = self.binary_to_int(most_common)
        epsilon_rate = self.binary_to_int(least_common)
        power_consumption = gamma_rate * epsilon_rate
        print(
            f'Power Consumption: {power_consumption} | Matches example: {power_consumption == Example.power_consumption}')

    def do_part_2(self, data):
        oxygen_generator = self.get_oxygen_generator(data)
        c02_scrubber = self.get_c02_scrubber(data)

        life_support_rating = oxygen_generator * c02_scrubber

        print(
            f'Life Support Rating: {life_support_rating} | Matches example: {life_support_rating == Example.life_support_rating}')

    def get_oxygen_generator(self, processed_input):
        for i, _ in enumerate(processed_input[0]):
            list_to_check = [item[i] for item in processed_input]
            most_common = Counter(list_to_check).most_common()
            most_common = 1 if most_common[0][1] == most_common[1][1] else most_common[0][0]
            processed_input = [item for item in processed_input if item[i] == most_common]
            if len(processed_input) == 1:
                break

        return self.binary_to_int(processed_input[0])

    def get_c02_scrubber(self, processed_input):
        for i, _ in enumerate(processed_input[0]):
            list_to_check = [item[i] for item in processed_input]
            most_common = Counter(list_to_check).most_common()
            least_common = 0 if most_common[-1][1] == most_common[-2][1] else most_common[-1][0]
            processed_input = [item for item in processed_input if item[i] == least_common]
            if len(processed_input) == 1:
                break

        return self.binary_to_int(processed_input[0])

    def get_most_common(self, lst, default=None):
        return [
            self.get_most_common_by_index(lst, i, default)
            for i, _ in enumerate(lst[0])
        ]

    def get_least_common(self, lst):
        return [
            self.get_least_common_by_index(lst, i)
            for i, _ in enumerate(lst[0])
        ]

    def process_input(self, raw_data) -> list:
        return [self.convert_string_to_list_of_ints(b.strip())
                for b
                in raw_data.splitlines()]

    @staticmethod
    def convert_string_to_list_of_ints(string):
        return [int(x) for x in string]

    @staticmethod
    def get_most_common_by_index(lst, index, default=None):
        list_to_check = [item[index] for item in lst]
        most_common = Counter(list_to_check).most_common()

        # print(most_common[0], most_common[1])

        if default and most_common[0][1] == most_common[1][1]:
            return default

        return most_common[0][0]

    @staticmethod
    def get_least_common_by_index(lst, index):
        list_to_check = [item[index] for item in lst]
        return Counter(list_to_check).most_common()[-1][0]

    def binary_to_int(self, digits):
        binary = self.get_binary(digits)
        return int(binary, 2)

    @staticmethod
    def get_binary(digits):
        return ''.join(str(i) for i in digits)

    def load_file(self, file):
        with open(file, 'r') as f_in:
            return f_in.read()


if __name__ == '__main__':
    app = BinaryDiagnostic()
    app.main()
