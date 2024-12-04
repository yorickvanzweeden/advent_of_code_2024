import re

from aoc import get_input


def main() -> None:
    data = get_input(3)
    multiplications = re.findall(r"mul\((\d+),(\d+)\)", data)
    result = sum([int(a) * int(b) for a, b in multiplications])
    print(result)


if __name__ == "__main__":
    main()
