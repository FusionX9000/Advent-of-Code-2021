from io import TextIOWrapper
from pathlib import Path
from typing import Dict, Generator, List, Tuple
from collections import defaultdict

Numbers = List[int]
Board = List[Numbers]
Boards = List[Board]
Game = Tuple[Numbers, Boards]
BoardState = Tuple[int, int]
BoardInfo = Tuple[int, int, int]

SIZE = 5

# Ignoring functional programming for sanity


def setup_states(boards: Boards) -> Tuple[Dict[int, BoardInfo], List[BoardState]]:
    num_map = defaultdict(list)

    for idx, board in enumerate(boards):
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                num_map[num].append((idx, i, j))

    board_states = [([0]*SIZE, [0]*SIZE) for _ in boards]
    return num_map, board_states


def update_and_get_winner(board_info: BoardInfo, board_states: List[BoardState]) -> Generator[int, None, None]:
    for board_idx, i, j in board_info:
        board_state = board_states[board_idx]
        row_counter, col_counter = board_state
        row_counter[i] += 1
        col_counter[j] += 1
        if(row_counter[i] == SIZE or col_counter[j] == SIZE):
            yield board_idx


def part1(game: Game) -> int:
    numbers, boards = game
    num_map, board_states = setup_states(boards)

    marked = set()

    for num in numbers:
        marked.add(num)
        for board_idx in update_and_get_winner(num_map[num], board_states):
            return num*sum(x for row in boards[board_idx] for x in row if x not in marked)


def part2(game: Game) -> int:
    numbers, boards = game
    num_map, board_states = setup_states(boards)

    marked = set()
    won = set()

    for num in numbers:
        marked.add(num)
        for board_idx in update_and_get_winner(num_map[num], board_states):
            won.add(board_idx)
            if len(won) == len(boards):
                return num*sum(x for row in boards[board_idx] for x in row if x not in marked)


def process_input(file: TextIOWrapper) -> Game:
    raw_input = [token for token in file.read().split("\n\n")]
    nums = [int(num) for num in raw_input[0].strip().split(",")]
    boards = [[[int(num) for num in line.strip().split()]
               for line in board.split("\n")] for board in raw_input[1:]]
    return (nums, boards)


if __name__ == "__main__":
    script_path = Path(__file__).resolve()
    input_path = script_path.parent / '../inputs' / f'{script_path.stem}.txt'

    with input_path.open('r') as f:
        data = process_input(f)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
