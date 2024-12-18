import re

from aoc import get_input

register: dict[str, int] = {
    "A": 0,
    "B": 0,
    "C": 0,
    "pointer": 0,
}


def convert_combo_operand(operand: int) -> int:
    match operand:
        case 0:
            return 0
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 3
        case 4:
            return register["A"]
        case 5:
            return register["B"]
        case 6:
            return register["C"]
        case 7:
            raise ValueError("Reserved")

    raise ValueError("Invalid operand")


def adv(operand: int) -> None:
    register["A"] = register["A"] >> convert_combo_operand(operand)


def bxl(operand: int) -> None:
    register["B"] ^= operand


def bst(operand: int) -> None:
    register["B"] = convert_combo_operand(operand) % 8


def jnz(operand: int) -> None:
    if register["A"] != 0:
        register["pointer"] = operand
        register["pointer"] -= 2


def bxc(_: int) -> None:
    register["B"] ^= register["C"]


def out(operand: int) -> int:
    return convert_combo_operand(operand) % 8


def bdv(operand: int) -> None:
    register["B"] = register["A"] >> convert_combo_operand(operand)


def cdv(operand: int) -> None:
    register["C"] = register["A"] >> convert_combo_operand(operand)


def calculate_program(program: list[int]) -> list[int]:
    op_codes = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}

    register["B"] = 0
    register["C"] = 0
    register["pointer"] = 0
    result = []

    while register["pointer"] < len(program):
        opcode = program[register["pointer"]]
        operand = program[register["pointer"] + 1]
        value = op_codes[opcode](operand)
        if value:
            result.append(value)

        register["pointer"] += 2

    return result


def main() -> None:
    data = get_input(17)

    register["A"] = int(re.search(r"Register A: (\d+)", data).group(1))  # type: ignore[union-attr]
    register["B"] = int(re.search(r"Register B: (\d+)", data).group(1))  # type: ignore[union-attr]
    register["C"] = int(re.search(r"Register C: (\d+)", data).group(1))  # type: ignore[union-attr]

    program = re.search(r"Program: (\d+(?:,\d+)*)", data).group(1)  # type: ignore[union-attr]
    program = list(map(int, program.split(",")))

    result = calculate_program(program)
    print(",".join(map(str, result)))


if __name__ == "__main__":
    main()
