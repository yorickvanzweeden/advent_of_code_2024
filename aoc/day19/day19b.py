from tqdm import tqdm

from aoc import get_input

cache: dict[str, int] = {}


def get_color_options(target: str, colors: list[str]) -> int:
    if not target:
        return 1

    if target in cache:
        return cache[target]

    cache[target] = 0
    for color in colors:
        if target.startswith(color):
            cache[target] += get_color_options(target[len(color) :], colors)

    return cache[target]


def main() -> None:
    data = get_input(19).splitlines()

    colors = data[0].split(", ")
    targets = [line.strip() for line in data[1:] if line.strip()]

    total = 0
    for target in tqdm(targets):
        possible = get_color_options(target, colors)
        total += int(possible)

    print(total)


if __name__ == "__main__":
    main()
