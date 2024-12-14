import re

from tqdm import tqdm

from aoc import get_input


def find_combination(
    a_x: int, a_y: int, b_x: int, b_y: int, target_x: int, target_y: int
) -> int | float:
    cache: dict[tuple[int, int], int | float] = {}

    def inner_loop(
        cost: int, p_x: int, p_y: int, a_pressed: int = 0, b_pressed: int = 0
    ) -> int | float:
        # Valid combination found, return cost
        if p_x == 0 and p_y == 0:
            return cost

        # Overshot, return max int
        if p_x < 0 or p_y < 0:
            return float("inf")

        # Memoization
        if (p_x, p_y) in cache:
            return cache[(p_x, p_y)]

        # Init to max int
        option_a = option_b = float("inf")

        # Options
        if a_pressed < 100:
            option_a = inner_loop(
                cost=cost + 3,
                p_x=p_x - a_x,
                p_y=p_y - a_y,
                a_pressed=a_pressed + 1,
                b_pressed=b_pressed,
            )

        if b_pressed < 100:
            option_b = inner_loop(
                cost=cost + 1,
                p_x=p_x - b_x,
                p_y=p_y - b_y,
                a_pressed=a_pressed,
                b_pressed=b_pressed + 1,
            )

        # Take min and cache
        result = min(option_a, option_b)
        cache[(p_x, p_y)] = result

        return result

    return inner_loop(0, target_x, target_y)


def main() -> None:
    data = get_input(13).strip()
    buttons_a = re.findall(r"Button A: X\+(\d+), Y\+(\d+)", data)
    buttons_b = re.findall(r"Button B: X\+(\d+), Y\+(\d+)", data)
    prices = re.findall(r"Prize: X=(\d+), Y=(\d+)", data)

    total_cost: int | float = 0
    for (a_x, a_y), (b_x, b_y), (p_x, p_y) in tqdm(
        zip(buttons_a, buttons_b, prices, strict=True), total=len(buttons_a)
    ):
        cost = find_combination(
            int(a_x), int(a_y), int(b_x), int(b_y), int(p_x), int(p_y)
        )
        if cost >= float("inf"):
            continue

        total_cost += cost

    print("Total", total_cost)


if __name__ == "__main__":
    main()
