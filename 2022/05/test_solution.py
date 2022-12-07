import pytest

from solution import load_input, prepare_data, solve_part_1, solve_part_2

FILE = "sample.txt"

PART_1_SAMPLE_ANSWER = "CMZ"
PART_2_SAMPLE_ANSWER = "MCD"


@pytest.fixture(scope="module")
def data() -> tuple:
    return prepare_data(load_input(file=FILE))


# @pytest.mark.skip
def test_solve_part_1(data, expected=PART_1_SAMPLE_ANSWER):
    assert solve_part_1(data) == expected


# @pytest.mark.skip
def test_solve_part_2(data, expected=PART_2_SAMPLE_ANSWER):
    assert solve_part_2(data) == expected
