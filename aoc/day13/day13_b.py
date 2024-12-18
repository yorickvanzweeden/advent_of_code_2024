import re

from aoc import get_input


def calculate_line_intersection(
    d_x1: int, d_y1: int, d_x2: int, d_y2: int, m_x: int, m_y: int
) -> tuple[int | None, int | None]:
    # line 1: y: ax
    a = d_y1 / d_x1

    # Line 2: y = bx + d
    b = d_y2 / d_x2

    # Calculate intersection and presses needed, losing the least precision
    a_pressed = (m_y - (d_y2 * m_x) / d_x2) / ((a - b) * d_x1)
    b_pressed = (a * m_x - m_y) / (d_x2 * (a - b))

    if (
        round(a_pressed) * d_x1 + round(b_pressed) * d_x2 != m_x
        or round(a_pressed) * d_y1 + round(b_pressed) * d_y2 != m_y
    ):
        return None, None

    return round(a_pressed), round(b_pressed)


def main() -> None:
    data = get_input(13).strip()

    buttons_a = re.findall(r"Button A: X\+(\d+), Y\+(\d+)", data)
    buttons_b = re.findall(r"Button B: X\+(\d+), Y\+(\d+)", data)
    prices = re.findall(r"Prize: X=(\d+), Y=(\d+)", data)

    total_cost = 0
    for (d_x1, d_y1), (d_x2, d_y2), (m_x, m_y) in zip(
        buttons_a, buttons_b, prices, strict=True
    ):
        offset = 10000000000000
        a, b = calculate_line_intersection(
            int(d_x1),
            int(d_y1),
            int(d_x2),
            int(d_y2),
            int(m_x) + offset,
            int(m_y) + offset,
        )

        if a and b:
            total_cost += 3 * a + b

    print("Total", total_cost)


#


if __name__ == "__main__":
    main()
