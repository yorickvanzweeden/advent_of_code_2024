import re

import numpy as np

from aoc import get_input


def check_line(line: list[str], depth: int = 0) -> bool:
    arr = np.array(line, dtype=int)
    diff = np.diff(arr)

    # Count positive / negative elements
    pos = np.count_nonzero(diff > 0)
    neg = np.count_nonzero(diff < 0)
    if neg > pos:
        diff = -diff

    # All values should be between 1 and 3

    # Get first value < 1 or > 3
    indices = np.where(np.any([diff < 1, diff > 3], axis=0))[0]

    if len(indices) == 0:
        return True

    if depth == 1:
        return False

    # Try fixing once
    index = indices[0]

    # Remove left from index
    option = line[: index - 1] + line[index:]
    if check_line(option, depth=1):
        return True

    # Remove index
    option = line[:index] + line[index + 1 :]
    if check_line(option, depth=1):
        return True

    # Remove right from index
    option = line[: index + 1] + line[index + 2 :]
    if check_line(option, depth=1):
        return True

    return False


def main() -> None:
    data = get_input(2).splitlines()

    number_lines = [re.split(r"\s+", line.strip()) for line in data]
    result = sum(map(check_line, number_lines))
    print(result)


if __name__ == "__main__":
    main()
