from aoc import get_input
from aoc.day21.day21a import get_shortest_length


def main() -> None:
    levels = 25
    data = get_input(21)

    lines = data.strip().splitlines()
    total = 0

    for line in lines:
        length = get_shortest_length(line, levels)
        total += int(line[:3]) * length
        print(line, length)

    print(total)


if __name__ == "__main__":
    main()
