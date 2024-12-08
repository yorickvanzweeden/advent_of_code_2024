import itertools
from collections import defaultdict

from aoc import get_input


def t_diff(t1: tuple[int, int], t2: tuple[int, int]) -> tuple[int, int]:
    return t1[0] - t2[0], t1[1] - t2[1]


def t_sum(t1: tuple[int, int], t2: tuple[int, int]) -> tuple[int, int]:
    return t1[0] + t2[0], t1[1] + t2[1]


def t_mul(t: tuple[int, int], k: int) -> tuple[int, int]:
    return t[0] * k, t[1] * k


def check(t: tuple[int, int], width: int, height: int) -> bool:
    if t[0] < 0 or t[1] < 0:
        return False
    if t[0] >= height:
        return False
    if t[1] >= width:
        return False
    return True


def calc_pos(k: int, t1: tuple[int, int], t2: tuple[int, int]) -> tuple[int, int]:
    return t_sum(t1, t_mul(t_diff(t1, t2), k))


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
            k_1 = 0
            while check(calc_pos(k_1, left, right), width, height):
                anti_nodes.add(str(calc_pos(k_1, left, right)))
                k_1 += 1

            k_2 = 0
            while check(calc_pos(k_2, right, left), width, height):
                anti_nodes.add(str(calc_pos(k_2, right, left)))
                k_2 += 1

    print(len(anti_nodes))


if __name__ == "__main__":
    main()
