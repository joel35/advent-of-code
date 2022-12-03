import pytest

import rucksack_reorganization

FILE = "sample.txt"


@pytest.fixture(scope="module")
def input_list() -> list:
    with open(FILE, "r") as f:
        return [x.strip() for x in f.readlines()]


@pytest.fixture
def p1_shared() -> list:
    return ["p", "L", "P", "v", "t", "s"]


@pytest.fixture
def p1_scores() -> list:
    return [16, 38, 42, 22, 20, 19]


@pytest.fixture
def p2_shared() -> list:
    return ["r", "Z"]


@pytest.fixture
def p2_scores() -> list:
    return [18, 52]


def test_p1_find_matching(input_list, p1_shared):
    func = rucksack_reorganization.p1_find_matching
    result = [func(x) for x in input_list]
    assert result == p1_shared


def test_get_score(p1_shared, p1_scores):
    func = rucksack_reorganization.get_score
    result = [func(x) for x in p1_shared]
    assert result == p1_scores


def test_solve_part_1(input_list, p1_shared, p1_scores):
    func = rucksack_reorganization.solve_part_1
    expected = 157
    assert func(input_list) == expected


def test_solve_part_2(input_list, p2_shared):
    func = rucksack_reorganization.solve_part_2
    expected = 70
    assert func(input_list) == expected

