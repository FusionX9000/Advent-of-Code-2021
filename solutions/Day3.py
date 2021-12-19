from io import TextIOWrapper
from pathlib import Path
from typing import Callable, List
from functools import reduce

# Sacrificing readability for terseness


def diff(bit):
    return 1 if bit == '1' else -1


def diff_as_binary(num: int):
    return '1' if num >= 0 else '0'


def part1(nums: List[str]) -> int:
    delta = reduce(lambda a, x: [
                   p+q for p, q in zip(a, [diff(v) for v in x])], nums, [0]*len(nums[0]))
    most = int("".join([diff_as_binary(x) for x in delta]), 2)
    return most*(most ^ 0xFFF)


def part2(nums: List[str]) -> int:
    def get_common_bit(nums, i) -> int:
        return diff_as_binary(reduce(lambda a, x: a+diff(x[i]), nums, 0))

    def solve(f: Callable[[List[str], int], int], nums: List[str], i) -> int:
        if len(nums) == 1:
            return int(nums[0], 2)
        filter_bit = f(nums, i)
        return int(nums[0], 2) if len(nums) == 1 else solve(f, list(filter(lambda x: x[i] == filter_bit, nums)), i+1)

    return solve(get_common_bit, nums, 0)*solve(lambda *args: str(int(get_common_bit(*args)) ^ 1), nums, 0)


def process_input(file: TextIOWrapper) -> List[str]:
    return file.read().splitlines()


if __name__ == "__main__":
    script_path = Path(__file__).resolve()
    input_path = script_path.parent / '../inputs' / f'{script_path.stem}.txt'

    with input_path.open('r') as f:
        data = process_input(f)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
