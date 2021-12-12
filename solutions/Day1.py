from io import TextIOWrapper
from pathlib import Path
from typing import List


def part1(depths: List[int]):
    return sum(d1 < d2 for d1, d2 in zip(depths, depths[1:]))


def part2(depths: List[int]):
    return part1(list(map(sum, zip(depths, depths[1:], depths[2:]))))


def process_input(file: TextIOWrapper):
    return [int(x) for x in file.read().splitlines()]


if __name__ == "__main__":
    script_path = Path(__file__).resolve()
    input_path = script_path.parent / '../inputs' / f'{script_path.stem}.txt'

    with input_path.open('r') as f:
        data = process_input(f)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
