#!/usr/bin/env python3

import logging
import os
import re
import subprocess
import sys
import tomllib
from dataclasses import dataclass
from functools import partial
from typing import Any

logger = logging.getLogger(__name__)


@dataclass
class Filter:
    paths: list[str]
    target: str

    @staticmethod
    def from_dict(value: dict[str, Any]) -> "Filter":
        return Filter(**value)


@dataclass
class Filters:
    filters: list[Filter]

    @staticmethod
    def from_dict(value: dict[str, Any]) -> "Filters":
        return Filters(list(map(Filter.from_dict, value["filters"])))


def changed_files() -> list[str]:
    result = subprocess.run(
        ["gh", "pr", "diff", "--name-only"],
        text=True,
        stdout=subprocess.PIPE,
    )
    logger.info(f"pr diff:\n{result.stdout}")
    result.check_returncode()
    return list(map(str.strip, result.stdout.split("\n")))


def filter_matches(filter: Filter, paths: list[str]) -> bool:
    for path in paths:
        for filter_pattern in filter.paths:
            if re.match(filter_pattern, path):
                return True
    return False


def set_output(
    name: str, filters: Filters, output_path: str = os.environ["GITHUB_OUTPUT"]
) -> None:
    value = "\n".join(map(lambda x: x.target, filters.filters))
    with open(output_path, "a") as file:
        file.write(f"{name}={value}")


def filters_match(filters: Filters, paths: list[str]) -> Filters:
    return Filters(list(filter(partial(filter_matches, paths=paths), filters.filters)))


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    filters = Filters.from_dict(tomllib.loads(sys.argv[1]))
    paths = changed_files()
    matched_filters = filters_match(filters, paths)
    set_output("targets", matched_filters)


if __name__ == "__main__":
    main()
