FILE = "input.txt"


def main():
    with open(FILE) as f_in:
        input = [line.strip() for line in f_in]

    do_part_1(input)
    do_part_2(input)


def do_part_1(input):
    part_1 = []
    for line in input:
        digits = [char for char in line if char.isnumeric()]

        num = int(digits[0] + digits[-1])
        part_1.append(num)

    print(f"Part 1: {sum(part_1)}")


def do_part_2(input):
    number_key = get_number_key()
    digits = (get_digits(line, number_key) for line in input)

    print(f"Part 2: {sum(digits)}")


def get_digits(line, number_key):
    first = find_first_digit(line, number_key)
    last = find_last_digit(line, number_key)
    return int("".join((first, last)))


def get_number_key():
    spelled = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    number_key = {word: str(i) for i, word in enumerate(spelled)}
    number_key.update({str(val): str(val) for val in range(10)})
    return number_key


def find_first_digit(line, number_key):
    for left in range(len(line)):
        for right in range(left + 1, len(line) + 1):
            check = line[left:right]
            if digit := number_key.get(check):
                return digit


def find_last_digit(line, number_key):
    for right in range(len(line), 0, -1):
        for left in range(right, -1, -1):
            check = line[left:right]
            # print(f'{left=} {right=} {check=}')
            if digit := number_key.get(check):
                return digit


if __name__ == "__main__":
    main()
