import networkx as nx

from aoc import get_input


def create_graph(data: list[str]) -> tuple[nx.DiGraph, set[str], set[str]]:
    graph = nx.DiGraph()

    starting_nodes = set()
    end_nodes = set()

    directions = {"left": (0, -1), "right": (0, 1), "up": (-1, 0), "down": (1, 0)}

    for y, line in enumerate(data):
        for x, cell in enumerate(line):
            node_name = f"({y},{x},{cell})"
            graph.add_node(node_name)

            if cell == "0":
                starting_nodes.add(node_name)
            elif cell == "9":
                end_nodes.add(node_name)

            for diff_y, diff_x in directions.values():
                other_y = y + diff_y
                other_x = x + diff_x

                if 0 <= other_y < len(data) and 0 <= other_x < len(line):
                    other_cell = data[other_y][other_x]
                    if int(other_cell) - int(cell) == 1:
                        new_node_name = (
                            f"({other_y},{other_x},{data[other_y][other_x]})"
                        )
                        graph.add_edge(node_name, new_node_name)

    return graph, starting_nodes, end_nodes


def main() -> None:
    data = get_input(10).strip().splitlines()

    graph, starting_nodes, end_nodes = create_graph(data)

    result = 0
    for start_node in starting_nodes:
        for end_node in end_nodes:
            result += int(nx.has_path(graph, start_node, end_node))

    print(result)


if __name__ == "__main__":
    main()
