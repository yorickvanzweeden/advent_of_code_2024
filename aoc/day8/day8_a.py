import itertools
from collections import defaultdict

from aoc import get_input


def t_diff(t1: tuple[int, int], t2: tuple[int, int]) -> tuple[int, int]:
    return t1[0] - t2[0], t1[1] - t2[1]


def t_sum(t1: tuple[int, int], t2: tuple[int, int]) -> tuple[int, int]:
    return t1[0] + t2[0], t1[1] + t2[1]


def check(t: tuple[int, int], width: int, height: int) -> bool:
    if t[0] < 0 or t[1] < 0:
        return False
    if t[0] >= height:
        return False
    if t[1] >= width:
        return False
    return True


def main() -> None:
    data = get_input(8).splitlines()

    width = len(data[0])
    height = len(data)

    # Get all locations
    positions = [
        (y, x, cell)
        for y, line in enumerate(data)
        for x, cell in enumerate(line)
        if cell != "."
    ]
    pos_map = defaultdict(list)
    for y, x, cell in positions:
        pos_map[cell].append((y, x))

    anti_nodes = set()
    for cell in pos_map.keys():
        combinations = itertools.combinations(pos_map[cell], 2)
        for left, right in combinations:
            pos_1 = t_sum(left, t_diff(left, right))
            pos_2 = t_sum(right, t_diff(right, left))
            if check(pos_1, width, height):
                anti_nodes.add(str(pos_1))
            if check(pos_2, width, height):
                anti_nodes.add(str(pos_2))

    print(len(anti_nodes))


if __name__ == "__main__":
    main()
