import networkx

from aoc import get_input


def find_components(
    lines: list[str], width: int, height: int, directions: dict[str, tuple[int, int]]
) -> list[set[tuple[int, int, str]]]:
    nodes = []
    edges = []

    for y, line in enumerate(lines):
        for x, cell in enumerate(line):
            current_position_tag = (y, x, cell)
            nodes.append(current_position_tag)

            for diff_y, diff_x in directions.values():
                other_y = y + diff_y
                other_x = x + diff_x

                if 0 <= other_y < height and 0 <= other_x < width:
                    if lines[other_y][other_x] == cell:
                        other_position_tag = (other_y, other_x, cell)
                        edges.append((current_position_tag, other_position_tag))

    graph = networkx.Graph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)

    # Find strongly connected components
    return list(networkx.connected_components(graph))


def find_border_components(
    component: set[tuple[int, int, str]],
    lines: list[str],
    width: int,
    height: int,
    directions: dict[str, tuple[int, int]],
) -> list[set[tuple[int, int]]]:
    border_nodes = set()
    border_edges = []

    for node in component:
        y, x, cell = node

        for _direction_name, direction in directions.items():
            other_y = y + direction[0]
            other_x = x + direction[1]

            if (
                0 <= other_y < height
                and 0 <= other_x < width
                and lines[other_y][other_x] == cell
            ):
                continue

            # We take direction / 4 to ensure that a corner has two sides
            # | *
            # | *
            # |  * * *
            # | ______
            border_node_tag = (y + direction[0] / 4, x + direction[1] / 4)
            border_nodes.add(border_node_tag)

    for border_node in border_nodes:
        for _direction_name, direction in directions.items():
            other_y_ = border_node[0] + direction[0]
            other_x_ = border_node[1] + direction[1]
            other_node = (other_y_, other_x_)
            if other_node in border_nodes:
                border_edges.append((border_node, other_node))

    border_graph = networkx.Graph()
    border_graph.add_nodes_from(border_nodes)
    border_graph.add_edges_from(border_edges)

    return list(networkx.connected_components(border_graph))


def main() -> None:
    data = get_input(12).strip()
    lines = data.splitlines()
    width = len(lines[0])
    height = len(lines)
    directions = {"left": (0, -1), "right": (0, 1), "up": (-1, 0), "down": (1, 0)}

    components = find_components(lines, width, height, directions)

    result = 0

    for component in components:
        border_components = find_border_components(
            component, lines, width, height, directions
        )
        result += len(border_components) * len(component)

    print(result)


if __name__ == "__main__":
    main()
