from io import TextIOWrapper
from pathlib import Path
from typing import Generic, List, TypeVar
from dataclasses import dataclass
from collections import Counter, defaultdict

T = TypeVar('T')


@dataclass(frozen=True)
class Point():
    x: int
    y: int


@dataclass(frozen=True)
class Pair(Generic[T]):
    first: T
    second: T


def intersects(pair1: Pair[Point], pair2: Pair[Point]) -> bool:
    a, b = pair1.first, pair1.second
    c, d = pair2.first, pair2.second

    return max(a.x, b.x) >= min(c.x, d.x) and min(a.x, b.x) <= max(c.x, d.x) and \
        max(a.y, b.y) >= min(c.y, d.y) and min(a.y, b.y) <= max(c.y, d.y)


def part1(pairs: List[Pair[Point]]) -> int:
    pairs = list(filter(lambda p: p.first.x ==
                        p.second.x or p.first.y == p.second.y, pairs))
    ans = 0
    for i, pair1 in enumerate(pairs):
        for j, pair2 in enumerate(pairs, i+1):
            ans += intersects(pair1, pair2)
    return ans

# TODO: Is there an easy way to find diagonal intersection in O(1) time?
# Time Complexity is different from part 1. O(N*MAX_DIST_BETWEEN_POINTS) instead of O(N^2) in part 1.


def part2(pairs: List[Pair[Point]]) -> int:
    intersections = defaultdict(int)
    for pair in pairs:
        a, b = pair.first, pair.second

        dx = 0 if a.x == b.x else (b.x-a.x)//abs(b.x-a.x)
        dy = 0 if a.y == b.y else (b.y-a.y)//abs(b.y-a.y)

        x, y = a.x, a.y
        intersections[(x, y)] += 1

        while x != b.x or y != b.y:
            x += dx
            y += dy
            intersections[(x, y)] += 1

    return sum(v > 1 for v in intersections.values())

# I was so preoccupied with whether or not I could do it, I didn't stop to think if I should.


def process_input(file: TextIOWrapper):
    return [Pair(*[Point(*[int(x) for x in coord.split(",")]) for coord in line.split(" -> ")]) for line in file.read().splitlines()]


if __name__ == "__main__":
    script_path = Path(__file__).resolve()
    input_path = script_path.parent / '../inputs' / f'{script_path.stem}.txt'

    with input_path.open('r') as f:
        data = process_input(f)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
