import argparse
from pathlib import Path

inputs_path = Path("./inputs")
solutions_path = Path("./solutions")


def get_new_day():
    created_days = set(int(path.stem.lower().replace("day", ""))
                       for path in solutions_path.iterdir())
    return next((day for day in range(1, 25) if day not in created_days), None)


def setup_parser():
    parser = argparse.ArgumentParser(description='Optional app description')
    parser.add_argument('day', type=int, nargs='?',
                        help='Day to be created')
    return parser


def verify(new_day):
    if new_day is None:
        raise ValueError("You've completed all 25 days")
    elif new_day > 25:
        raise ValueError(f"Invalid argument, {new_day} arg exeeds 25")


def create_files(new_day):
    soln_path = solutions_path / f"Day{new_day}.py"
    input_path = inputs_path / f"Day{new_day}.txt"

    if not soln_path.exists():
        with soln_path.open("w") as f:
            f.write(template)
        input_path.touch()
    else:
        raise FileExistsError("Day already exists!")


if __name__ == "__main__":
    with open("template.py", "r") as f:
        template = f.read()
    parser = setup_parser()

    new_day = parser.parse_args().day or get_new_day()

    verify(new_day)

    create_files(new_day)
