import os
from typing import Tuple

import pandas

path = "data"


def load_text_file(filename) -> str:
    """
    Loads a text file and returns the text as a string.
    """
    with open(filename, "r") as f:
        return f.read()


def load_delta_file(filename) -> Tuple[pandas.DataFrame, ...]:
    """
    Loads a delta file and returns the text as a string.
    """
    header = []

    with open(filename, "r") as f:
        header_str = f.readline()
        for line in f.readlines():
            split = line.split("|")
            for line in split:
                header.append(line.strip())


with os.scandir(path) as it:
    for entry in it:
        if entry.name.endswith(".txt") and entry.is_file():
            if entry.name.startswith("deltaWmass"):
                print(entry.name)
                print(load_text_file(entry.path))
                # pass
            else:
                print(entry.name)
                # print(load_text_file(entry.path))
