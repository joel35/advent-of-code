#!/usr/bin/env python3
#  https://adventofcode.com/2022/day/5


FILE = "input.txt"


def main():
    data = load_input()
    p1_data = prepare_data(data)
    print(f"PART 1: {solve_part_1(p1_data)}")
    p2_data = prepare_data(data)
    print(f"PART 2: {solve_part_2(p2_data)}")


def load_input(file=FILE) -> list:
    with open(file, "r") as f:
        return [line for line in f.readlines()]


def prepare_data(data) -> tuple:
    split_index = data.index("\n")

    sorted_crates = []

    for row in data[: split_index - 1]:
        row = row.replace("    ", " [.] ")
        columns = [c.strip("[] \n") for c in row.split(" ") if not c in ("", "\n")]
        columns = [None if c == '.' else c for c in columns]
        sorted_crates.append(columns)

    n_stacks = int(data[split_index - 1].strip()[-1])

    stacks = [[] for _ in range(n_stacks)]

    for i in range(len(sorted_crates) - 1, -1, -1):
        for j, stack in enumerate(stacks):
            if crate := sorted_crates[i][j]:
                stack.append(crate)

    sorted_instructions = []

    for instruction in [i.strip() for i in data[split_index + 1:]]:
        instruction = instruction.replace("move ", "").replace("from ", "").replace("to ", "").strip().split()
        instruction = [int(i) for i in instruction]

        sorted_instructions.append(
            tuple([instruction[0], instruction[1] - 1, instruction[2] - 1])
        )

    return stacks, sorted_instructions


def solve_part_1(data: tuple[list, list]):
    stacks, instructions = data
    # print("Start")
    # for stack in stacks:
    #     print(stack)

    for i, (n_crates, from_i, to_i) in enumerate(instructions, 1):

        for _ in range(n_crates):
            if stacks[from_i]:
                crate = stacks[from_i].pop()
                stacks[to_i].append(crate)

        # print()
        # print(f"Step {i}: Move {n_crates} from {from_i+1} to {to_i+1}")
        # for j, stack in enumerate(stacks, 1):
        #     print(f"{j} {stack}")

    return ''.join([stack[-1] if stack else ' ' for stack in stacks])


def solve_part_2(data):
    stacks, instructions = data
    # print("Start")
    # for stack in stacks:
    #     print(stack)

    for i, (n_crates, from_i, to_i) in enumerate(instructions, 1):
        buffer = []

        for _ in range(n_crates):
            if stacks[from_i]:
                buffer.append(stacks[from_i].pop())

        while buffer:
            stacks[to_i].append(buffer.pop())

        # print()
        # print(f"Step {i}: Move {n_crates} from {from_i+1} to {to_i+1}")
        # for j, stack in enumerate(stacks, 1):
        #     print(f"{j} {stack}")

    return ''.join([stack[-1] if stack else '' for stack in stacks])


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
