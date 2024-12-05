#!/usr/bin/env python3
# https://adventofcode.com/...

from collections import defaultdict
from pathlib import Path

FILE = "input.txt"
# FILE = "sample.txt"


def main():
    data = load_input()
    print(f"PART 1: {solve_part_1(data)}")
    print(f"PART 2: {solve_part_2(data)}")


def load_input(file: str = FILE) -> list:
    path = Path(__file__).with_name(file)
    with open(path, "r") as f:
        return [line.strip() for line in f]


def solve_part_1(data: list) -> int:
    rules, updates = parse_input(data)
    goods, _ = check_updates(updates, rules)
    return sum_middles(goods)
            
        
def solve_part_2(data: list) -> int:
    rules, updates = parse_input(data)
    _, bads = check_updates(updates, rules)
    
    for bad in bads:
        i = 1
        while i < len(bad):
            if i < 1 or not (rule := rules.get(bad[i])):
                i += 1
                continue

            if bad[i-1] in rule:
                bad.insert(i, bad.pop(i-1))
                i -= 1
                continue
            
            i += 1

    return sum_middles(bads)

def parse_input(data: list) -> tuple[dict, list]:
    div = data.index('')
    rules = [tuple(map(int, r.split('|'))) for r in data[:div]]
    rules_dict = defaultdict(list)
    for key, value in rules:
        rules_dict[key].append(value)

    updates = [list(map(int, u.split(','))) for u in data[div+1:]]

    return rules_dict, updates


def check_updates(updates: list, rules: dict) -> tuple:
    good = []
    bad = []

    for update in updates:
        good_flag = True
        stack = update.copy()
        
        while stack:
            if not (after := rules.get(stack.pop())):
                continue

            if [u for u in stack if u in after]:
                good_flag = False
                bad.append(update)
                break
        
        if good_flag:
            good.append(update)
        
    return good, bad

def sum_middles(data: list) -> int:
    return sum(d[len(d) // 2] for d in data)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
