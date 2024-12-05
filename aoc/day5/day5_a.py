import re
from collections import defaultdict

from aoc import get_input


def main() -> None:
    data = get_input(5)

    rules, updates = re.split(r"\n\n", data)
    rules = [list(map(int, r.split("|"))) for r in rules.strip().splitlines()]
    rules_map = defaultdict(set)
    for l, r in rules:
        rules_map[l].add(r)

    updates = updates.strip().splitlines()
    updates = [list(map(int, update.split(","))) for update in updates]

    result = 0
    for update in updates:
        doubles = zip(update, update[1:], strict=False)
        failure = False
        for a, b in doubles:
            if a in rules_map[b]:
                failure = True
        if not failure:
            result += update[len(update) // 2]
    print(result)


if __name__ == "__main__":
    main()
