import networkx

from aoc import get_input
from aoc.day18.day18a import build_graph


def main() -> None:
    data = get_input(18).splitlines()

    # Apply binary search to find
    i = 0
    j = len(data)

    while True:
        if j - i == 1:
            break
        index = (i + j) // 2
        print(i, index, j)
        graph, start, end = build_graph(data[:index])

        try:
            networkx.shortest_path_length(graph, source=start, target=end)
        except networkx.exception.NetworkXNoPath:
            # Too many walls, reduce data length
            j = index
        else:
            # Too few walls, increase data length
            i = index

    print("First coordinate to block:", data[i])


if __name__ == "__main__":
    main()
