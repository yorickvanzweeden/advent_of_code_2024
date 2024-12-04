import re

from aoc import get_input


def main() -> None:
    data = get_input(3)
    multiplications = re.findall(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", data)

    result = 0
    mul_enabled = True

    for command, a, b in multiplications:
        op = command.split("(")[0]
        if op == "mul" and mul_enabled:
            result += int(a) * int(b)
        elif op == "do":
            mul_enabled = True
        elif op == "don't":
            mul_enabled = False

    print(result)


if __name__ == "__main__":
    main()
