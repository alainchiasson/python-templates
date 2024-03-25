#!/usr/bin/env python3
from __future__ import annotations

import argparse
import asyncio
from collections.abc import Sequence


async def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    # Add arguments here
    args = parser.parse_args(argv)

    # Implement behaviour here

    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
