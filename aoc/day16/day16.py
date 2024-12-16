import matplotlib.pyplot as plt
import networkx
from networkx import Graph

from aoc import get_input


def draw_path(graph: Graph, start: tuple[int, int, str], end: tuple[int, int]) -> None:
    plt.figure()
    plt.grid(True)
    plt.gca().invert_yaxis()

    for node in graph.nodes:
        if node in [start, end]:
            plt.plot(node[1], node[0], "bo")
        else:
            plt.plot(node[1], node[0], "ro")

    for edge in graph.edges:
        plt.plot(
            [edge[0][1], edge[1][1]],
            [edge[0][0], edge[1][0]],
            color="gray",
            linestyle="--",
        )

    path = networkx.shortest_path(graph, source=start, target=end, weight="weight")

    for first, second in zip(path[1:-1], path[2:], strict=False):
        plt.plot([first[1], second[1]], [first[0], second[0]], "g-")
    for node in path:
        plt.plot(node[1], node[0], "go")
    plt.show()


def main() -> None:
    data = get_input(16)

    grid_raw = data.strip().splitlines()
    height = len(grid_raw)
    width = len(grid_raw[0])

    nodes = set()
    edges = set()
    start = end = None

    direction_map = {(0, 1): "right", (0, -1): "left", (1, 0): "down", (-1, 0): "up"}
    inverse_map = {"left": "right", "right": "left", "up": "down", "down": "up"}

    for y, line in enumerate(grid_raw):
        for x, cell in enumerate(line):
            if cell == "#":
                continue
            if cell == "S":
                start = (y, x, "right")  # Start is facing East
            if cell == "E":
                end = (y, x)

            # Create map of direction: node
            others = {}
            for (dy, dx), direction in direction_map.items():
                ny, nx = y + dy, x + dx
                if ny < 0 or ny >= height or nx < 0 or nx >= width:
                    continue
                if grid_raw[ny][nx] != "#":
                    others[direction] = [ny, nx]

            for direction, other in others.items():
                nodes.add((y, x, direction))
                other_node = tuple(other + [inverse_map[direction]])
                edges.add(((y, x, direction), other_node, 0))

            # If up & down -> Add edge (weight=1)
            if "up" in others and "down" in others:
                edges.add(((y, x, "up"), (y, x, "down"), 1))

            # If left & right -> Add edge (weight=1)
            if "left" in others and "right" in others:
                edges.add(((y, x, "left"), (y, x, "right"), 1))

            other_directions = set(others.keys())
            for direction_in in other_directions:
                for direction_out in other_directions - {
                    direction_in,
                    inverse_map[direction_in],
                }:
                    edges.add(((y, x, direction_in), (y, x, direction_out), 1001))

    # Add start node
    if start not in nodes and start is not None:
        # Find all nodes that are in the same position as start
        same_pos = [node for node in nodes if node[:2] == start[:2]]
        nodes.add(start)
        for node in same_pos:
            edges.add((start, node, 1 if node[2] == "left" else 1001))

    # Add empty end node
    if not end:
        raise ValueError("End not found")
    same_end_pos = [node for node in nodes if node[:2] == end]
    nodes.add(end)  # type: ignore[arg-type]
    for node in same_end_pos:
        edges.add((end, node, 0))  # type: ignore[arg-type]

    # Calculate path length
    graph = Graph()
    graph.add_nodes_from(nodes)
    graph.add_weighted_edges_from(edges)
    path_length = networkx.shortest_path_length(
        graph, source=start, target=end, weight="weight"
    )
    print(f"Path length: {path_length}")

    # Calculate number of nodes in shortest paths
    paths = networkx.all_shortest_paths(
        graph, source=start, target=end, weight="weight"
    )
    path_nodes = set()
    for path in paths:
        for y, x, _ in path[:-1]:
            path_nodes.add((y, x))

    print(len(path_nodes))

    # Draw graph
    # draw_path(graph, start, end)


if __name__ == "__main__":
    main()
