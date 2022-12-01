# https://adventofcode.com/2021/day/1
from dataclasses import dataclass


@dataclass
class SonarSweep:
    file = 'input.txt'
    test_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    part_1_answer = 7
    part_2_answer = 5
    sensor_readings: list = None

    def main(self):
        self.sensor_readings = self.get_sensor_readings(self.file)

        print(self.part_1())
        print(self.part_2())

    @staticmethod
    def get_sensor_readings(file):
        with open(file, 'r') as f_in:
            return [int(reading) for reading in f_in.read().strip().splitlines()]

    def part_1(self):
        test = self.count_measurement_increases(self.test_input)

        if test != self.part_1_answer:
            raise RuntimeError

        return self.count_measurement_increases(self.sensor_readings)

    @staticmethod
    def count_measurement_increases(readings):
        return sum(n1 < n2
                   for n1, n2
                   in zip(readings, readings[1:])
                   )

    def part_2(self):
        test_readings = self.add_three_consecutive_readings(self.test_input)
        test = self.count_measurement_increases(test_readings)
        if test != self.part_2_answer:
            raise RuntimeError

        readings = self.add_three_consecutive_readings(self.sensor_readings)
        return self.count_measurement_increases(readings)

    @staticmethod
    def add_three_consecutive_readings(readings):
        output = zip(readings, readings[1:], readings[2:])
        return [sum(list(o)) for o in output]


if __name__ == '__main__':
    app = SonarSweep()
    app.main()
