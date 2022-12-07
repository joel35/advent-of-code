import pytest

from solution import solve_part_1, solve_part_2


@pytest.fixture(
    scope="module",
    params=[
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7, 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5, 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6, 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10, 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11, 26),
    ]
)
def data(request) -> list:
    yield request.param


def test_solve_part_1(data):
    input_, expected, _ = data
    assert solve_part_1(input_) == expected


def test_solve_part_2(data):
    input_, _, expected = data
    assert solve_part_2(input_) == expected
