import re

from aoc import get_input


def main() -> None:
    data = get_input(1).splitlines()

    lines = [re.split(r"\s+", line.strip()) for line in data]
    left, right = list(zip(*lines, strict=True))
    left = sorted(map(int, left))
    right = sorted(map(int, right))

    acc = 0

    for l, r in zip(left, right, strict=True):
        acc += abs(l - r)

    print(acc)


if __name__ == "__main__":
    main()
