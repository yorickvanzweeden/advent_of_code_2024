import re

from aoc import get_input

# from aoc import get_input


def move(
    grid: list[list[str]], robot_pos: tuple[int, int], direction: tuple[int, int]
) -> tuple[list[list[str]], tuple[int, int]]:
    y, x = robot_pos
    dy, dx = direction

    target_pos = y + dy, x + dx
    legal = False

    while True:
        cell = grid[target_pos[0]][target_pos[1]]

        # Hit a wall
        if cell == "#":
            legal = False
            break

        # Available space to move
        if cell == ".":
            legal = True
            break

        # Found a box
        target_pos = target_pos[0] + dy, target_pos[1] + dx

    # No legal move, as we hit a wall
    if not legal:
        return grid, robot_pos

    # Execute shift by 1 in direction up to target_pos
    if dy != 0:
        for y in range(target_pos[0], robot_pos[0], -dy):
            grid[y][target_pos[1]] = grid[y - dy][target_pos[1]]
    else:
        for x in range(target_pos[1], robot_pos[1], -dx):
            grid[target_pos[0]][x] = grid[target_pos[0]][x - dx]

    # Reset robot pos square
    grid[robot_pos[0]][robot_pos[1]] = "."

    # New robot pos
    robot_pos = (robot_pos[0] + dy, robot_pos[1] + dx)

    return grid, robot_pos


def display_grid(grid: list[list[str]]) -> None:
    for line in grid:
        for cell in line:
            # Print wall in red
            # Print robot in green
            # Print box in blue
            if cell == "#":
                print("\033[91m" + cell, end="\033[0m")
            elif cell == "@":
                print("\033[92m" + cell, end="\033[0m")
            elif cell == "O":
                print("\033[94m" + cell, end="\033[0m")
            else:
                print(cell, end="")
        print()

    print("\033[0m")


def main() -> None:
    data = get_input(15)
    grid_raw, directions = data.strip().split("\n\n")
    grid = [list(line) for line in grid_raw.strip().splitlines()]

    dir_map = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}

    # Find robot
    robot_pos = [
        (y, x)
        for y, line in enumerate(grid)
        for x, cell in enumerate(line)
        if cell == "@"
    ][0]

    directions = re.sub(r"\s+", "", directions)
    for direction in directions:
        grid, robot_pos = move(grid, robot_pos, dir_map[direction])
        # display_grid(grid)

    box_total = 0
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if cell == "O":
                box_total += 100 * y + x

    print("Box total", box_total)


if __name__ == "__main__":
    main()
