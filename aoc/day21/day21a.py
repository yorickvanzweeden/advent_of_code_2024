from functools import cache

import networkx
from networkx.classes import Graph

from aoc import get_input

dirpad = {
    ("<", "<"): "A",
    ("<", ">"): ">>A",
    ("<", "^"): ">^A",
    ("<", "A"): ">>^A",
    ("<", "v"): ">A",
    (">", "<"): "<<A",
    (">", ">"): "A",
    (">", "^"): "<^A",
    (">", "A"): "^A",
    (">", "v"): "<A",
    ("^", "<"): "v<A",
    ("^", ">"): "v>A",
    ("^", "^"): "A",
    ("^", "A"): ">A",
    ("^", "v"): "vA",
    ("A", "<"): "v<<A",
    ("A", ">"): "vA",
    ("A", "^"): "<A",
    ("A", "A"): "A",
    ("A", "v"): "<vA",
    ("v", "<"): "<A",
    ("v", ">"): ">A",
    ("v", "^"): "^A",
    ("v", "A"): "^>A",
    ("v", "v"): "A",
}

directions = {
    (0, -1): "^",
    (0, 1): "v",
    (-1, 0): "<",
    (1, 0): ">",
}

numpad = {
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "0": (1, 3),
    "A": (2, 3),
}


@cache
def get_sequence_length(segment: str, level: int) -> int:
    if level == 0:
        return len(segment)

    # Add the starting point
    sequence = "A" + segment

    # Take the sequence in pairs
    segments = zip(sequence, sequence[1:], strict=False)

    # Sum the lengths of the segments (recursively)
    return sum(get_sequence_length(dirpad[(a, b)], level - 1) for a, b in segments)


def get_graph() -> Graph:
    graph = Graph()

    nodes = set(numpad.values())
    graph.add_nodes_from(nodes)

    for x, y in nodes:
        for dx, dy in directions.keys():
            new_x = x + dx
            new_y = y + dy
            if (new_x, new_y) in nodes:
                graph.add_edge((x, y), (new_x, new_y))

    return graph


def get_shortest_length(line: str, levels: int) -> int:
    graph = get_graph()
    nodes = [numpad["A"]] + [numpad[c] for c in line]
    final_length = 0

    for start, end in zip(nodes, nodes[1:], strict=False):
        shortest_length = float("inf")

        paths = networkx.all_shortest_paths(graph, source=start, target=end)
        for path in paths:
            # Convert path to directions
            path = [
                directions[(path[i + 1][0] - path[i][0], path[i + 1][1] - path[i][1])]
                for i in range(len(path) - 1)
            ]

            length = get_sequence_length("".join(path) + "A", level=levels)
            if length < shortest_length:
                shortest_length = length

        final_length += int(shortest_length)

    return final_length


def main() -> None:
    levels = 2
    data = get_input(21)

    lines = data.strip().splitlines()
    total = 0

    for line in lines:
        length = get_shortest_length(line, levels)
        total += int(line[:3]) * length
        print(line, length)

    print(total)


if __name__ == "__main__":
    main()
