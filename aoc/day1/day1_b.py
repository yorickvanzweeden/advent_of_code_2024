import re
from collections import Counter

from aoc import get_input


def main() -> None:
    data = get_input(1).splitlines()

    lines = [re.split(r"\s+", line.strip()) for line in data]
    left, right = list(zip(*lines, strict=True))
    left = map(int, left)
    right = map(int, right)

    counter = Counter(right)

    acc = 0

    for l in left:
        acc += l * counter.get(l, 0)

    print(acc)


if __name__ == "__main__":
    main()
