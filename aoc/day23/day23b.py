import networkx
from networkx.classes import Graph

from aoc import get_input


def main() -> None:
    data = get_input(23)

    lines = data.strip().splitlines()
    graph = Graph()

    for line in lines:
        a, b = line.split("-")
        graph.add_node(a)
        graph.add_node(b)
        graph.add_edge(a, b)

    all_cliques = list(networkx.find_cliques(graph))
    max_clique = max(all_cliques, key=len)
    print(",".join(sorted(max_clique)))


if __name__ == "__main__":
    main()
