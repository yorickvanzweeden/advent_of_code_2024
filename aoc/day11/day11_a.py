import math
from functools import cache

from aoc import get_input


@cache
def apply_rules(number: int) -> tuple[int, ...]:
    if number == 0:
        return (1,)

    digits = math.floor(math.log10(number)) + 1
    if digits % 2 == 0:
        div = int(math.pow(10, digits // 2))
        left = number // div
        right = number % div
        return left, right

    return (number * 2024,)


@cache
def calculate(number: int, depth: int) -> int:
    if depth == 0:
        return 1

    result = 0
    for n in apply_rules(number):
        result += calculate(n, depth - 1)

    return result


def main() -> None:
    data = get_input(11).strip().split()

    result = 0
    for number in data:
        result += calculate(int(number), 25)

    print(result)


if __name__ == "__main__":
    main()
