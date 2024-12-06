from aoc import get_input


def sum_t(t1: tuple[int, int], t2: tuple[int, int]) -> tuple[int, int]:
    return t1[0] + t2[0], t1[1] + t2[1]


def main() -> None:
    data = get_input(6).splitlines()
    starting_position = [
        (y, x)
        for y, line in enumerate(data)
        for x, char in enumerate(line)
        if char in ["^", "v", "<", ">"]
    ][0]
    starting_direction = data[starting_position[0]][starting_position[1]]

    # Reset item at starting position
    data[starting_position[0]] = (
        data[starting_position[0]][: starting_position[1]]
        + "."
        + data[starting_position[0]][starting_position[1] + 1 :]
    )

    directions = {
        "^": (-1, 0),
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1),
    }
    turn_right = {
        "^": ">",
        ">": "v",
        "v": "<",
        "<": "^",
    }
    current_direction = starting_direction
    current_position = starting_position
    positions_visited = set(str(current_position))

    while True:
        new_pos = sum_t(current_position, directions[current_direction])
        if new_pos[0] < 0 or new_pos[1] < 0:
            break
        if new_pos[0] >= len(data) or new_pos[1] >= len(data[0]):
            break
        # Continue forward
        if data[new_pos[0]][new_pos[1]] == ".":
            positions_visited.add(str(new_pos))
            current_position = new_pos
            continue
        # Turn right
        current_direction = turn_right[current_direction]

    print(len(positions_visited))


if __name__ == "__main__":
    main()
