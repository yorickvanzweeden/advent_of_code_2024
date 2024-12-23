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
    all_three_cliques = []
    for clique in all_cliques:
        if len(clique) < 3:
            continue
        if len(clique) == 3:
            all_three_cliques.append(clique)
        else:
            import itertools

            for comb in itertools.combinations(clique, 3):
                all_three_cliques.append(comb)

    all_three_cliques_set = set([str(sorted(clique)) for clique in all_three_cliques])
    all_three_cliques = [
        eval(clique) for clique in all_three_cliques_set  # noqa: PGH001
    ]
    count = 0
    for clique in all_three_cliques:
        for node in clique:
            if node.startswith("t"):
                count += 1
                break
    print(count)


if __name__ == "__main__":
    main()
