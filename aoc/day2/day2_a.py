import re

import numpy as np

from aoc import get_input


def check_line(line: list[str]) -> bool:
    arr = np.array(line, dtype=int)
    diff = np.diff(arr)
    min_diff = np.min(diff)
    max_diff = np.max(diff)

    if min(abs(min_diff), abs(max_diff)) < 1:
        return False

    if max(abs(min_diff), abs(max_diff)) > 3:
        return False

    if min_diff < 0 and max_diff < 0:
        return True

    if min_diff > 0 and max_diff > 0:
        return True

    return False


def main() -> None:
    data = get_input(2).splitlines()

    number_lines = [re.split(r"\s+", line.strip()) for line in data]
    result = sum(map(check_line, number_lines))
    print(result)


if __name__ == "__main__":
    main()
