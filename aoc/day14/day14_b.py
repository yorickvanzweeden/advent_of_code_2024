import re

import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm

from aoc import get_input


def display_coords(x_coords: list[int], y_coords: list[int], t: int) -> None:
    # Create the scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(x_coords, y_coords)

    # Invert the y-axis
    plt.gca().invert_yaxis()

    # Add labels and title
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title(f"Points at t={t}")

    plt.grid(True)

    plt.show()

    # Close
    plt.close()


def main() -> None:
    data = get_input(14).splitlines()
    lines = [
        (int(x), int(y), int(vx), int(vy))
        for x, y, vx, vy in [re.findall(r"-?\d+", line) for line in data]
    ]

    width = 101
    height = 103

    std_scores = []
    for t in tqdm(range(10000)):
        x_coords = []
        y_coords = []
        for x, y, vx, vy in lines:
            x_coords.append((x + vx * t) % width)
            y_coords.append((y + vy * t) % height)

        std_x = np.std(x_coords)
        if std_x < 24 or std_x > 35:
            std_y = np.std(y_coords)
            if std_y < 24 or std_y > 35:
                std_scores.append((t, std_x))
                display_coords(x_coords, y_coords, t)

    # Plot std scores
    plt.figure(figsize=(8, 6))
    plt.scatter(*zip(*std_scores, strict=True))
    plt.show()


if __name__ == "__main__":
    main()
