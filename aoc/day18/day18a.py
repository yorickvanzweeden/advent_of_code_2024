import matplotlib.pyplot as plt
import networkx
from networkx import Graph

from aoc import get_input


def draw_path(
    graph: Graph, start: tuple[int, int, str], end: tuple[int, int, str]
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
        plt.plot(node[1], node[0], "go")
    plt.show()


def build_graph(
    data: list[str],
) -> tuple[Graph, tuple[int, int, str], tuple[int, int, str]]:
    height = 71
    width = 71

    grid_raw = ["." * width] * height
    for line in data:
        x, y = map(int, line.split(","))
        grid_raw[y] = grid_raw[y][:x] + "#" + grid_raw[y][x + 1 :]

    nodes = set()
    edges = set()

    start = (0, 0, "empty")
    end = (height - 1, width - 1, "empty")

    direction_map = {(0, 1): "right", (0, -1): "left", (1, 0): "down", (-1, 0): "up"}

    for y, line in enumerate(grid_raw):
        for x, cell in enumerate(line):
            if cell == "#":
                nodes.add((y, x, "wall"))
                continue

            nodes.add((y, x, "empty"))

            # Create map of direction: node
            for (dy, dx), _direction in direction_map.items():
                ny, nx = y + dy, x + dx
                if ny < 0 or ny >= height or nx < 0 or nx >= width:
                    continue
                if grid_raw[ny][nx] != "#":
                    edges.add(((y, x, "empty"), (ny, nx, "empty")))

    graph = Graph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)

    return graph, start, end


def main() -> None:
    data = get_input(18).splitlines()[:1024]
    graph, start, end = build_graph(data)

    print(networkx.shortest_path_length(graph, source=start, target=end))

    # Draw graph
    draw_path(graph, start, end)


if __name__ == "__main__":
    main()
