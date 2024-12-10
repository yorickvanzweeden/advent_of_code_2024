import networkx as nx
from day10.day10_a import create_graph
from tqdm import tqdm

from aoc import get_input


def main() -> None:
    data = get_input(10).strip().splitlines()

    graph, starting_nodes, end_nodes = create_graph(data)

    result = 0
    for start_node in tqdm(starting_nodes):
        for end_node in end_nodes:
            result += len(list(nx.all_simple_paths(graph, start_node, end_node)))

    print(result)


if __name__ == "__main__":
    main()
