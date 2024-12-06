from tqdm import tqdm

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
    loop_count = 0

    for y in tqdm(range(len(data))):
        for x in range(len(data[0])):
            if data[y][x] == "X":
                continue
            if (y, x) == starting_position:
                continue

            data_backup = data.copy()
            data[y] = data[y][:x] + "X" + data[y][x + 1 :]
            current_position = starting_position
            current_direction = starting_direction

            positions_visited = set()
            positions_visited.add(str(current_position + tuple(current_direction)))

            while True:
                new_pos = sum_t(current_position, directions[current_direction])
                indexed_value = str(new_pos + tuple(current_direction))
                if indexed_value in positions_visited:
                    loop_count += 1
                    break

                if new_pos[0] < 0 or new_pos[1] < 0:
                    break
                if new_pos[0] >= len(data) or new_pos[1] >= len(data[0]):
                    break

                # Continue forward
                if (
                    data[new_pos[0]][new_pos[1]] == "."
                    or data[new_pos[0]][new_pos[1]] == "O"
                ):
                    positions_visited.add(indexed_value)
                    data[new_pos[0]] = (
                        data[new_pos[0]][: new_pos[1]]
                        + "O"
                        + data[new_pos[0]][new_pos[1] + 1 :]
                    )
                    current_position = new_pos
                    continue

                # Turn right
                current_direction = turn_right[current_direction]

            data = data_backup.copy()
    print(loop_count)


if __name__ == "__main__":
    main()
