#!/usr/bin/env python
from __future__ import annotations

import argparse
from contextlib import closing
from collections.abc import Sequence
from io import TextIOWrapper


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", action="store_true", dest="number")
    parser.add_argument("file", type=argparse.FileType("r"), nargs="+")
    args = parser.parse_args(argv)

    number: bool = args.number
    files: list[TextIOWrapper] = args.file

    for file in files:
        with closing(file):
            for i, line in enumerate(file, start=1):
                if number:
                    print(f"{i: >6} ", end="")
                print(line, end="")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
