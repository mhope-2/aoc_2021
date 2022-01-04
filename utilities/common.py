import os
from pathlib import Path
ROOT_PATH = Path(__file__).resolve().parent.parent


def convert_to_list(input_file):
    with open(os.path.join(ROOT_PATH, input_file), 'r') as input_file:
        return [int(number) for number in list(input_file.readlines()) ]
