import pytest

from solution import load_input, solve_part_1, solve_part_2

FILE = "sample.txt"

PART_1_SAMPLE_ANSWER = 95437
PART_2_SAMPLE_ANSWER = None


@pytest.fixture(scope="module")
def data() -> list:
    return load_input(file=FILE)


def test_solve_part_1(data, expected=PART_1_SAMPLE_ANSWER):
    assert solve_part_1(data) == expected


@pytest.mark.skip
def test_solve_part_2(data, expected=PART_2_SAMPLE_ANSWER):
    assert solve_part_2(data) == expected
