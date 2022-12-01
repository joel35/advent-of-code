def main():
    data = load_data('example_input')
    print(f'Part 1: {do_part_1(data)}')
    data = load_data('input')
    print(do_part_2(data))


def do_part_1(data):
    return sum(
        len([digit for digit in digits if len(digit) in [2, 3, 4, 7]])
        for digits in [entry['output'] for entry in data]
    )


def do_part_2(data):
    lengths = {
        2: 1,
        4: 4,
        3: 7,
        7: 8
    }

    answer = 0

    for entry in data:
        pattern = [''.join(sorted(p)) for p in entry['pattern']]
        output = [''.join(sorted(o)) for o in entry['output']]

        print(pattern)
        values = {i: None for i in range(10)}

        for p in pattern:
            number = lengths.get(len(p))
            if number:
                values[number] = p

        for p in pattern:
            if len(p) == 5 and all(char in p for char in values[7]):
                values[3] = p
            if len(p) == 6 and all(char in p for char in values[4]):
                values[9] = p
            if (
                len(p) == 6
                and all(char in p for char in values[7])
                and any(char not in p for char in values[4])
            ):
                values[0] = p

        for p in pattern:
            if (
                    len(p) == 5
                    and all(char in values[9] for char in p)
                    and any(char not in p for char in values[1])
            ):
                values[5] = p

        remaining = [p for p in pattern if p not in values.values()]

        for p in remaining:
            if len(p) == 5:
                values[2] = p
            else:
                values[6] = p
        print(values)

        new_key = {v: k for k, v in values.items()}

        # print(new_key)
        print(output)
        value = int(''.join(str(new_key[word]) for word in output))
        answer += value
        print()
    return answer


def load_data(file: str):
    with open(file, 'r') as f_in:
        return [
            dict(pattern=a.split(), output=b.split())
            for a, b
            in [item.split(' | ')
                for item
                in f_in.readlines()]
        ]


if __name__ == '__main__':
    main()
