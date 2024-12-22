from tqdm import tqdm

from aoc import get_input


def main() -> None:
    rounds = 2000
    data = get_input(22)

    numbers = list(map(int, data.strip().splitlines()))
    total = 0
    for number in tqdm(numbers):
        value = number
        for _r in range(rounds):
            # Shift 6, XOR, take first 24 bits
            value = value ^ (value << 6) % 16777216

            # Downshift 5, XOR, take first 24 bits
            value = value ^ (value >> 5) % 16777216

            #
            value = value ^ (value << 11) % 16777216

        total += value

    print(total)


if __name__ == "__main__":
    main()
