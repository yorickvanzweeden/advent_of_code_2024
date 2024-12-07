from tqdm import tqdm

from aoc import get_input


def dfs(target: int, total: int, items: list[int], index: int) -> bool:
    if total > target:
        return False
    if index == len(items):
        if total == target:
            return True
        return False

    path_mul = dfs(target, total * items[index], items, index + 1)
    path_add = dfs(target, total + items[index], items, index + 1)

    # Join op
    if index > 0:
        join_num = int(str(total) + str(items[index]))
        path_join = dfs(target, join_num, items, index + 1)
    else:
        path_join = False

    return path_mul or path_add or path_join


def main() -> None:
    data = get_input(7).splitlines()
    line_items = [line.split(": ") for line in data]
    result = 0

    for _i, (target, items_raw) in tqdm(enumerate(line_items)):
        items = [int(x) for x in items_raw.split(" ")]
        if dfs(int(target), items[0], items, 1):
            result += int(target)

    print(result)


if __name__ == "__main__":
    main()
