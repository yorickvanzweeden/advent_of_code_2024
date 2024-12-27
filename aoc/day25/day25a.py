import itertools

from aoc import get_input


def convert(value: str) -> tuple[str, list[int]]:
    lines = value.strip().splitlines()

    if all([c == "#" for c in lines[0]]):
        type_ = "lock"
        del lines[0]
    else:
        type_ = "key"
        del lines[-1]

    # Transpose 2D array
    transposed: list[list[str]] = list(map(list, zip(*lines, strict=False)))  # type: ignore[no-untyped-call]
    amounts = [col.count("#") for col in transposed]

    return type_, amounts


def main() -> None:
    data = get_input(25)

    segments = data.strip().split("\n\n")
    locks = set()
    keys = set()
    for segment in segments:
        type_, amounts = convert(segment)
        if type_ == "lock":
            locks.add(tuple(amounts))
        else:
            keys.add(tuple(amounts))

    # Use itertools to get all combinations
    valid = 0
    combinations = itertools.product(keys, locks)
    for key, lock in combinations:
        # Sum per element
        if all([k + l <= 5 for k, l in zip(key, lock, strict=True)]):
            valid += 1
            print(key, lock)

    print(valid)


if __name__ == "__main__":
    main()
