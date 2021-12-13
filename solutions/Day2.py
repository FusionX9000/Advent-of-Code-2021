from io import TextIOWrapper
from pathlib import Path
from typing import List, Tuple
from functools import reduce
from operator import mul
from collections import namedtuple


def part1(commands: List[Tuple[str, int]]) -> int:
    mapper = {
        "forward": lambda x: (0, x),
        "down": lambda x: (x, 0),
        "up": lambda x: (-x, 0)
    }
    return reduce(mul, (sum(x) for x in zip(*[mapper[cmd[0]](cmd[1]) for cmd in commands])), 1)


def part2(commands: List[Tuple[str, int]]) -> int:
    State = namedtuple('State', 'x, y, aim')

    def accumulator(state: State, command: Tuple[str, int]):
        match command:
            case ["forward", n]:
                return State(state.x+n, state.y+state.aim*n, state.aim)
            case ["down", n]:
                return State(state.x, state.y, state.aim+n)
            case ["up", n]:
                return State(state.x, state.y, state.aim-n)

    final_state: State = reduce(accumulator, commands, State(0, 0, 0))
    return final_state.x*final_state.y


def process_input(file: TextIOWrapper) -> List[Tuple[str, int]]:
    return [(cmd, int(val)) for cmd, val in [line.split() for line in [line.strip() for line in file.readlines()]]]


if __name__ == "__main__":
    script_path = Path(__file__).resolve()
    input_path = script_path.parent / '../inputs' / f'{script_path.stem}.txt'

    with input_path.open('r') as f:
        data = process_input(f)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
