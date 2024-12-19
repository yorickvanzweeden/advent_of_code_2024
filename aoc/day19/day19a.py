from tqdm import tqdm

from aoc import get_input

cache: dict[str, bool] = {}


def get_color_options(target: str, colors: list[str]) -> bool:
    if not target:
        return True

    if target in cache:
        return cache[target]

    for color in colors:
        if target.startswith(color):
            cache[target] = get_color_options(target[len(color) :], colors)
            if cache[target]:
                return True

    return False


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
