from io import TextIOWrapper
from pathlib import Path
from typing import List

# THe optimal position would be where most of the crabs lie, i.e. their median


def part1(positions: List[int]) -> int:
    positions = sorted(positions)
    median = positions[len(positions)//2]
    return sum(abs(pos-median) for pos in positions)

# The optimal position might not be the position of any one crab anymore


def part2(positions: List[int]) -> int:
    def arithmetic_sum(n): return n*(n+1)//2
    def cost(p): return sum(arithmetic_sum(abs(p-pos)) for pos in positions)
    return min(cost(pos) for pos in range(min(positions), max(positions)+1))


def process_input(file: TextIOWrapper) -> List[int]:
    return [int(x) for x in file.read().split(",")]


if __name__ == "__main__":
    script_path = Path(__file__).resolve()
    input_path = script_path.parent / '../inputs' / f'{script_path.stem}.txt'

    with input_path.open('r') as f:
        data = process_input(f)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
