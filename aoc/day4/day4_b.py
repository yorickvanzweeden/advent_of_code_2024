from aoc import get_input


def get_item(
    data: list[str], origin: tuple[int, int], delta: tuple[int, int]
) -> str | None:
    pos = (origin[0] + delta[0], origin[1] + delta[1])

    if pos[0] < 0 or pos[1] < 0:
        return None
    try:
        return data[pos[0]][pos[1]]
    except IndexError:
        return None


def main() -> None:
    data = get_input(4).splitlines()

    x_positions = [
        (i, j)
        for i, line in enumerate(data)
        for j, char in enumerate(line)
        if char == "A"
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

    combination = [("Up-Left", "Down-Right"), ("Up-Right", "Down-Left")]

    count = 0

    for i, j in x_positions:
        found = 0

        for pair in combination:
            # Convert direction tuple to delta
            direction_l = directions[pair[0]]
            direction_r = directions[pair[1]]
            required_chars = {"M", "S"}

            chars_found = {
                get_item(data, (i, j), direction_l[0]),
                get_item(data, (i, j), direction_r[0]),
            }
            if chars_found != required_chars:
                continue

            found += 1

        if found == 2:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
