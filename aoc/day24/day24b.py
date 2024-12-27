import re

import graphviz as gv

from aoc import get_input


def get_shape_color(op: str) -> tuple[str, str]:
    match op:
        case "AND":
            return "trapezium", "blue"
        case "OR":
            return "diamond", "red"
        case "XOR":
            return "invtriangle", "green"
        case _:
            return "box", "black"


def main() -> None:
    data = get_input(24)
    _, connections = data.strip().split("\n\n")

    dot = gv.Digraph()

    for a, op, b, c in re.findall(r"(.+) (.+) (.+) -> (.+)", connections):
        dot.node(a)
        dot.node(b)
        dot.node(c)

        order = (min(a, b), max(a, b), c, op)
        shape, color = get_shape_color(op)
        dot.node(str(order), label=op, shape=shape, color=color)
        dot.edge(a, str(order))
        dot.edge(b, str(order))
        dot.edge(str(order), c)

    # As png
    dot.render("day24b", format="png", cleanup=True)


if __name__ == "__main__":
    main()
