import networkx

from aoc import get_input


def main() -> None:
    lines = get_input(12).strip().splitlines()
    width = len(lines[0])
    height = len(lines)

    directions = {"left": (0, -1), "right": (0, 1), "up": (-1, 0), "down": (1, 0)}

    nodes = []
    edges = []

    for y, line in enumerate(lines):
        for x, cell in enumerate(line):
            current_position_tag = f"{y} {x} {cell}"
            nodes.append(current_position_tag)

            for diff_y, diff_x in directions.values():
                other_y = y + diff_y
                other_x = x + diff_x

                if 0 <= other_y < height and 0 <= other_x < width:
                    if lines[other_y][other_x] == cell:
                        other_position_tag = f"{other_y} {other_x} {cell}"
                        edges.append((current_position_tag, other_position_tag))

    graph = networkx.Graph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)

    # Find strongly connected components
    components = list(networkx.connected_components(graph))

    result = 0

    for component in components:
        area = len(component)
        total_perimeter = 0

        for node in component:
            y_str, x_str, cell = node.split()
            y, x = int(y_str), int(x_str)
            perimeter = 4

            for direction in directions.values():
                other_y = y + direction[0]
                other_x = x + direction[1]

                if (
                    0 <= other_y < height
                    and 0 <= other_x < width
                    and lines[other_y][other_x] == cell
                ):
                    perimeter -= 1

            total_perimeter += perimeter

        result += area * total_perimeter

    print(result)


if __name__ == "__main__":
    main()
