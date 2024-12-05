import re
from collections import defaultdict

from aoc import get_input


def main() -> None:
    data = get_input(5)

    # Parse rules
    rules, updates = re.split(r"\n\n", data)
    rules = [list(map(int, r.split("|"))) for r in rules.strip().splitlines()]
    rules_map = defaultdict(set)
    for l, r in rules:
        rules_map[l].add(r)

    updates = updates.strip().splitlines()
    updates = [list(map(int, update.split(","))) for update in updates]

    # Find incorrect updates
    failed_updates = []
    for update in updates:
        failure = False
        doubles = zip(update, update[1:], strict=False)
        for a, b in doubles:
            if a in rules_map[b]:
                failure = True

        if failure:
            failed_updates.append(update)

    # Fix failed updates
    result = 0
    for update in failed_updates:
        while True:
            doubles = zip(update, update[1:], strict=False)
            swap_occurred = False
            for i, (a, b) in enumerate(doubles):
                if a in rules_map[b]:
                    # Swap pair
                    update[i] = b
                    update[i + 1] = a
                    swap_occurred = True
                    break

            # When no swaps have occurred, the update is ordered correctly
            if not swap_occurred:
                break

        result += update[len(update) // 2]

    print(result)


if __name__ == "__main__":
    main()
