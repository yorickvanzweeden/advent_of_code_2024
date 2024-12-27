import re

import networkx
from networkx.classes import DiGraph

from aoc import get_input


def process_op(value1: int, value2: int, op: str) -> int:
    match op:
        case "OR":
            return value1 or value2
        case "AND":
            return value1 and value2
        case "XOR":
            return value1 ^ value2
        case _:
            raise ValueError("Op unknown")


def main() -> None:
    data = get_input(24)
    values_raw, connections_ = data.strip().split("\n\n")
    values_parsed = re.findall(r"(...): (\d)", values_raw)
    connections = re.findall(r"(.+) (.+) (.+) -> (.+)", connections_)
    connections_map = {}

    values = {k: int(v) for k, v in values_parsed}
    has_outgoing = set()

    # Create compute graph
    graph = DiGraph()
    for connection in connections:
        a, op, b, c = connection
        graph.add_node(a, value=values.get(a, None))
        graph.add_node(b, value=values.get(b, None))
        graph.add_node(c, value=values.get(c, None))
        graph.add_edge(a, c, op=op)
        graph.add_edge(b, c, op=op)
        connections_map[c] = (a, b, op)
        has_outgoing.add(a)
        has_outgoing.add(b)

    # Draw graph
    import matplotlib.pyplot as plt

    networkx.draw(graph, with_labels=True)
    plt.show()

    # Find root node using topological sort
    topological_sort = networkx.topological_sort(graph)
    for node in topological_sort:
        if node in values:
            continue

        in_node_1, in_node_2, op = connections_map[node]
        values[node] = process_op(values[in_node_1], values[in_node_2], op)

    bits_to_check = set(values.keys()) - has_outgoing
    output = [values[bit] for bit in sorted(bits_to_check, reverse=True)]
    print(int("".join(map(str, output)), 2))


if __name__ == "__main__":
    main()
