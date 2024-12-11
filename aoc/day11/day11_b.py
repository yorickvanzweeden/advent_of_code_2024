from day11.day11_a import calculate

from aoc import get_input


def main() -> None:
    data = get_input(11).strip().split()

    result = 0
    for number in data:
        result += calculate(int(number), 75)

    print(result)


if __name__ == "__main__":
    main()
