from io import TextIOWrapper
from pathlib import Path
from typing import List


def simulate_day(state: List[int]) -> List[int]:
    # Extremely dangerous. Do not try this at work without professional supervision.
    return [*state[1:7], state[7]+state[0], state[8], state[0]]


def solve(days: int, timers: List[int]) -> int:
    state = [0]*9

    for timer in timers:
        state[timer] += 1

    for _ in range(days):
        state = simulate_day(state)

    return sum(state)


def part1(timers: List[int]) -> int:
    return solve(80, timers)


def part2(timers: List[int]) -> int:
    return solve(256, timers)


def process_input(file: TextIOWrapper) -> List[int]:
    return [int(x) for x in file.read().split(",")]


if __name__ == "__main__":
    script_path = Path(__file__).resolve()
    input_path = script_path.parent / '../inputs' / f'{script_path.stem}.txt'

    with input_path.open('r') as f:
        data = process_input(f)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
