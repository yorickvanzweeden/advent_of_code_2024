import re
from collections import deque

from aoc import get_input

# from aoc import get_input


def move(
    grid: list[list[str]], robot_pos: tuple[int, int], direction: tuple[int, int]
) -> tuple[list[list[str]], tuple[int, int]]:
    # Queue for tracking which positions to check
    transactions = deque([robot_pos])

    # This collection will be used for moving
    to_move = {robot_pos: 1}

    legal = False

    while transactions:
        y, x = transactions.popleft()
        dy, dx = direction
        target_pos = y + dy, x + dx
        cell = grid[target_pos[0]][target_pos[1]]

        # Hit a wall
        if cell == "#":
            legal = False
            break

        # Available space to move
        if cell == ".":
            legal = True
            continue

        # Found a box
        transactions.append(target_pos)
        to_move[target_pos] = 1

        # Check box alignment when moving vertically
        if direction[0] != 0:
            if cell == "[":
                other_pos = (target_pos[0], target_pos[1] + 1)
            else:
                other_pos = (target_pos[0], target_pos[1] - 1)

            transactions.append(other_pos)
            to_move[other_pos] = 1

    if not legal:
        # print("Not legal")
        return grid, robot_pos

    # Move is legal, process to_move in reversed order
    dy, dx = direction

    for y, x in reversed(to_move.keys()):
        new_pos = y + dy, x + dx
        grid[new_pos[0]][new_pos[1]] = grid[y][x]
        grid[y][x] = "."

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
            elif cell == "[" or cell == "]":
                print("\033[94m" + cell, end="\033[0m")
            else:
                print(cell, end="")
        print()

    print("\033[0m")


def transform_grid(grid: list[list[str]]) -> list[list[str]]:
    new_grid = []
    for line in grid:
        new_line = []
        for cell in line:
            match cell:
                case "#":
                    new_line.extend(["#"] * 2)
                case ".":
                    new_line.extend(["."] * 2)
                case "@":
                    new_line.extend(["@", "."])
                case "O":
                    new_line.extend(["[", "]"])
                case _:
                    raise ValueError("Unrecognized cell type", cell)
        new_grid.append(new_line)

    return new_grid


def main() -> None:
    data = get_input(15)
    grid_raw, directions = data.strip().split("\n\n")
    grid = [list(line) for line in grid_raw.strip().splitlines()]
    # display_grid(grid)
    grid = transform_grid(grid)
    # display_grid(grid)

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
        # print("Direction", direction)
        grid, robot_pos = move(grid, robot_pos, dir_map[direction])
        # display_grid(grid)

    box_total = 0
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if cell == "[":
                box_total += 100 * y + x

    print("Box total", box_total)


if __name__ == "__main__":
    main()
