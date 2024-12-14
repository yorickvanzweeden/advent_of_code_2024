import re

from aoc import get_input


def main() -> None:
    data = get_input(14).splitlines()

    width = 101
    height = 103

    quadrant_count = [0 for _ in range(4)]

    for line in data:
        x, y, vx, vy = map(int, re.findall(r"-?\d+", line))
        p_x, p_y = ((x + vx * 100) % width, (y + vy * 100) % height)

        if p_x < width // 2 and p_y < height // 2:
            quadrant_count[0] += 1
        elif p_x > width // 2 and p_y < height // 2:
            quadrant_count[1] += 1
        elif p_x < width // 2 and p_y > height // 2:
            quadrant_count[2] += 1
        elif p_x > width // 2 and p_y > height // 2:
            quadrant_count[3] += 1

    product = (
        quadrant_count[0] * quadrant_count[1] * quadrant_count[2] * quadrant_count[3]
    )

    print(product)


if __name__ == "__main__":
    main()
