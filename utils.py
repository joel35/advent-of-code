def load_input(file: str) -> list:
    path = Path(__file__).with_name(file)
    with open(path) as f:
        return [line.strip() for line in f]