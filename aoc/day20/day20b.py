from aoc import get_input
from aoc.day20.day20a import build_graph, find_savings


def main() -> None:
    data = get_input(20)
    graph, start, end = build_graph(data)
    count = find_savings(graph, start, end, shortcut_length=20, threshold=100)
    print(count)


if __name__ == "__main__":
    main()
