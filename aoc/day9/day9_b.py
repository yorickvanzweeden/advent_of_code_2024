from collections import defaultdict

from aoc import get_input


def compose_order(
    files_rle: list[int],
    free_rle: list[int],
    positions: dict[int, list[tuple[int, int]]],
) -> list[int | str]:
    # Compose order
    order: list[int | str] = []
    for free_index in range(len(files_rle)):
        order += [free_index] * files_rle[free_index]
        for j, file_count in positions.get(free_index, []):
            order += [j] * file_count
        if free_index < len(free_rle):
            order += ["."] * free_rle[free_index]

    # print("".join(map(str,order)))
    return order


def main() -> None:
    data = get_input(9).strip()
    data = "2333133121414131402"
    diskmap = [int(c) for c in data]
    files_rle = [count for i, count in enumerate(diskmap) if i % 2 == 0]
    free_rle = [count for i, count in enumerate(diskmap) if i % 2 == 1]
    largest_free_space = max(free_rle)

    positions: dict[int, list[tuple[int, int]]] = defaultdict(list)
    compose_order(files_rle, free_rle, positions)

    for file_index, file_count in reversed(list(enumerate(files_rle))):
        for free_index, free_count in enumerate(free_rle):
            # Skip if file is unmovable
            if file_count > largest_free_space:
                break

            # We have moved past the original index of the file, no move to the left is possible
            if free_index >= file_index:
                break

            # File fits in gap
            if file_count <= free_count:
                # Note where the file will be placed
                positions[free_index].append((file_index, file_count))

                # Reduce free space at dest
                free_rle[free_index] -= file_count

                # Assign free space b/c of file move
                free_rle[file_index - 1] += file_count

                # Merge with next free space slot
                if file_index < len(free_rle) and not positions.get(2, False):
                    free_rle[file_index - 1] += free_rle[file_index]
                    free_rle[file_index] = 0

                # Remove file
                files_rle[file_index] -= file_count

                compose_order(files_rle, free_rle, positions)
                break

    order = compose_order(files_rle, free_rle, positions)
    print(sum(i * c for i, c in enumerate(order) if isinstance(c, int)))


if __name__ == "__main__":
    main()
