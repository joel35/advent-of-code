#!/usr/bin/env python3
#  https://adventofcode.com/2022/day/07

FILE = "input.txt"


def main():
    data = load_input()
    print(f"PART 1: {solve_part_1(data)}")
    print(f"PART 2: {solve_part_2(data)}")


def load_input(file=FILE) -> list:
    with open(file, "r") as f:
        return [line.strip() for line in f.readlines()]


def solve_part_1(data):
    tree = {}
    dir_stack = []
    current_dir = None

    for output in data:
        print(output)
        match output.split():
            case ["$", "cd", ".."]:
                dir_stack.pop()

            case["$", "cd", dir_]:
                dir_stack.append(dir_)

            case ["$", "ls"]:
                # create tree branch using dir_stack & assign to `current_dir`
                pass

            case ["dir", directory]:
                # add dir to branch
                # current_dir[directory] = {}
                pass

            case [*file]:
                # add file to branch
                # current_dir[file[1]] = int(file[0])
                pass

        print(dir_stack)




def solve_part_2(data):
    pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
