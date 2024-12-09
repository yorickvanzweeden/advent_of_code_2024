from collections import deque

from line_profiler_pycharm import profile

from aoc import get_input


@profile
def main() -> None:
    data = get_input(9).strip()

    diskmap = [int(c) for c in data]

    # Double sided queue
    files_rle = [count for i, count in enumerate(diskmap) if i % 2 == 0]
    files = deque([c for i, count in enumerate(files_rle) for c in [i] * count])

    order = [
        files.popleft() if i % 2 == 0 else files.pop()
        for i, count in enumerate(diskmap)
        for _ in range(count)
        if len(files)
    ]

    print(sum([i * c for i, c in enumerate(order)]))


if __name__ == "__main__":
    main()
