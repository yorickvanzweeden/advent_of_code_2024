from tqdm import tqdm

from aoc import get_input


def main() -> None:
    rounds = 2000
    data = get_input(22)

    numbers = list(map(int, data.strip().splitlines()))
    sequences = []

    for number in tqdm(numbers):
        new_sequence = [number % 10]
        value = number
        for _r in range(rounds):
            # Shift 6, XOR, take first 24 bits
            value = value ^ (value << 6) % 16777216

            # Downshift 5, XOR, take first 24 bits
            value = value ^ (value >> 5) % 16777216

            # Shift 11, XOR, take first 24 bits
            value = value ^ (value << 11) % 16777216

            new_sequence.append(value % 10)

        sequences.append(new_sequence)

    # Calculate diffs
    diffs = []
    for sequence in sequences:
        diff = []
        for i in range(1, len(sequence)):
            diff.append(sequence[i] - sequence[i - 1])
        diffs.append(diff)

    # Take 4, and corresponding price
    prices: dict[int, dict[str, int]] = {}
    for number, sequence, diff in zip(numbers, sequences, diffs, strict=True):
        prices[number] = {}
        for i in range(4, len(diff)):
            h = str(diff[i - 4 : i])
            if h not in prices[number]:
                prices[number][h] = sequence[i]

    # Sum dicts
    final_price = {}
    for price in prices.values():
        for key, value in price.items():
            if key not in final_price:
                final_price[key] = 0
            final_price[key] += value

    # Get max price
    max_price = max(final_price.values())
    print(max_price)


if __name__ == "__main__":
    main()
