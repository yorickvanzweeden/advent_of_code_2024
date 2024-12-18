import re

from aoc import get_input
from aoc.day17.day17a import calculate_program, register


def recursive(program: list[int], current: str) -> str:
    if len(current) // 3 == len(program):
        return current

    options = []
    for register_a in range(8):
        register_a_bits = f"{register_a:03b}"
        # Convert to binary in 3x format
        register["A"] = int(current + register_a_bits, 2)
        result = calculate_program(program)
        if result == program[-len(result) :]:
            options.append(recursive(program, current + register_a_bits))

    return max(options, key=lambda x: len(x)) if options else current


def main() -> None:
    data = get_input(17)

    program = re.search(r"Program: (\d+(?:,\d+)*)", data).group(1)  # type: ignore[union-attr]
    program = list(map(int, program.split(",")))

    register_a_bits = recursive(program, "")
    register["A"] = int(register_a_bits, 2)
    print(register["A"])
    result = calculate_program(program)
    print(result)


if __name__ == "__main__":
    main()
