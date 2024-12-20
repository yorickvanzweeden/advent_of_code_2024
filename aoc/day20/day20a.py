import networkx
from matplotlib import pyplot as plt
from networkx.classes import Graph
from tqdm import tqdm

from aoc import get_input


def draw_path(
    graph: Graph,
    start: tuple[int, int, str],
    end: tuple[int, int, str],
    distance: int = 0,
) -> None:
    plt.figure()
    plt.grid(True)
    plt.gca().invert_yaxis()

    for node in graph.nodes:
        if node in [start, end]:
            plt.plot(node[1], node[0], "bo")
        elif node[2] == "wall":
            plt.plot(node[1], node[0], "ro")
        else:
            plt.plot(node[1], node[0], "yo")

    for edge in graph.edges:
        plt.plot(
            [edge[0][1], edge[1][1]],
            [edge[0][0], edge[1][0]],
            color="gray",
            linestyle="--",
        )

    path = networkx.shortest_path(graph, source=start, target=end)

    for first, second in zip(path[1:-1], path[2:], strict=False):
        plt.plot([first[1], second[1]], [first[0], second[0]], "g-")
    for node in path:
        if node in [start, end]:
            plt.plot(node[1], node[0], "bo")
        else:
            plt.plot(node[1], node[0], "go")

    plt.title(f"Path length: {len(path) - 1 + distance}")
    plt.show()


def build_graph(data: str) -> tuple[Graph, tuple[int, int, str], tuple[int, int, str]]:
    lines = data.strip().splitlines()

    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }
    height = len(lines)
    width = len(lines[0])

    nodes = set()
    edges = set()

    start, end = None, None

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                nodes.add((y, x, "wall"))
                continue

            if char == "S":
                start = (y, x, "node")
            elif char == "E":
                end = (y, x, "node")

            nodes.add((y, x, "node"))

            for dy, dx in directions.values():
                ny, nx = y + dy, x + dx
                if 0 <= ny < height and 0 <= nx < width and lines[ny][nx] != "#":
                    edges.add(((y, x, "node"), (ny, nx, "node")))

    graph = Graph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)

    if start is None or end is None:
        raise ValueError("Start or end not found")

    return graph, start, end


def find_savings(
    graph: Graph,
    start: tuple[int, int, str],
    end: tuple[int, int, str],
    shortcut_length: int,
    threshold: int,
) -> int:
    shortest_path = networkx.shortest_path(graph, start, end)
    shortest_path_indexed = {node: i for i, node in enumerate(shortest_path)}

    path_length = networkx.shortest_path_length(graph, start, end)
    print("Current shortest path", path_length)
    # draw_path(graph, start, end)

    processed = set()

    count = 0
    for node in tqdm(shortest_path):
        processed.add(node)

        for other_node in shortest_path:
            # Skip if node is the same as other_node
            if node == other_node:
                continue

            # Prevent double counting
            if other_node in processed:
                continue

            distance = abs(node[0] - other_node[0]) + abs(node[1] - other_node[1])

            # Skip if shortcut is too long
            if distance > shortcut_length:
                continue

            index_distance = (
                abs(shortest_path_indexed[node] - shortest_path_indexed[other_node]) - 1
            )
            # This will not save time
            if index_distance <= distance:
                continue

            savings = index_distance - distance + 1

            if savings >= threshold:
                count += 1

    return count


def main() -> None:
    data = get_input(20)
    graph, start, end = build_graph(data)
    count = find_savings(graph, start, end, shortcut_length=2, threshold=100)
    print(count)


if __name__ == "__main__":
    main()
