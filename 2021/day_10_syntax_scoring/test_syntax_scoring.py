import pytest

import syntax_scoring


@pytest.fixture
def part_1():
    return syntax_scoring.Part1()


@pytest.fixture
def part_2():
    return syntax_scoring.Part2()


@pytest.mark.parametrize('line, illegal', [
    ("[({(<(())[]>[[{[]{<()<>>", None),
    ("{([(<{}[<>[]}>{[]{[(<()>", "}"),
    ("[[<[([]))<([[{}[[()]]]", ")"),
    ("[{[{({}]{}}([{[{{{}}([]", "]"),
    ("[<(<(<(<{}))><([]([]()", ")"),
    ("<{([([[(<>()){}]>(<<{{", ">")
])
def test_get_illegal(part_1, line, illegal):
    return_value = part_1.get_illegal(line)
    assert return_value == illegal


@pytest.mark.parametrize('illegals, score', [
    (["}", ")", "]", ")", ">"], 26397)
])
def test_get_illegals_score(part_1, illegals, score):
    return_value = part_1.get_score(illegals)
    assert return_value == score


@pytest.mark.parametrize('line, closer', [
    ("[({(<(())[]>[[{[]{<()<>>", "}}]])})]"),
    ("[(()[<>])]({[<{<<[]>>(", ")}>]})"),
    ("(((({<>}<{<{<>}{[]{[]{}", "}}>}>))))"),
    ("{<[[]]>}<{[{[{[]{()[[[]", "]]}}]}]}>"),
    ("<{([{{}}[<[[[<>{}]]]>[]]", "])}>")
])
def test_get_closers(part_2, line, closer):
    return_value = part_2.get_closers(line)
    assert return_value == closer


@pytest.mark.parametrize('string, score', [
    ("])}>", 294),
    ("}}]])})]", 288957),
    (")}>]})", 5566),
    ("}}>}>))))", 1480781),
    ("]]}}]}]}>", 995444),
    ("])}>", 294)
])
def test_get_closers_score(part_2, string, score):
    return_value = part_2.get_score(string)
    assert return_value == score


@pytest.mark.parametrize('scores, middle', [
    ([288957, 5566, 1480781, 995444, 294], 288957)
])
def test_find_middle_score(part_2, scores, middle):
    return_value = part_2.get_middle_score(scores)
    assert return_value == middle
