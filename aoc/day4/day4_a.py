from aoc import get_input


def main() -> None:
    data = get_input(4).splitlines()

    x_positions = [
        (i, j)
        for i, line in enumerate(data)
        for j, char in enumerate(line)
        if char == "X"
    ]

    directions = {
        "Left": [(0, -1), (0, -2), (0, -3)],
        "Right": [(0, 1), (0, 2), (0, 3)],
        "Up": [(-1, 0), (-2, 0), (-3, 0)],
        "Down": [(1, 0), (2, 0), (3, 0)],
        "Up-Left": [(-1, -1), (-2, -2), (-3, -3)],
        "Up-Right": [(-1, 1), (-2, 2), (-3, 3)],
        "Down-Left": [(1, -1), (2, -2), (3, -3)],
        "Down-Right": [(1, 1), (2, 2), (3, 3)],
    }

    count = 0

    for i, j in x_positions:
        for direction, direction_delta in directions.items():
            required_chars = ["M", "A", "S"]
            for delta, char in zip(direction_delta, required_chars, strict=True):
                pos = (i + delta[0], j + delta[1])
                if pos[0] < 0 or pos[1] < 0:
                    continue
                try:
                    if data[pos[0]][pos[1]] != char:
                        break
                    if char == "S":
                        count += 1
                        print((i, j), direction)
                except IndexError:
                    break

    print(count)


if __name__ == "__main__":
    main()
