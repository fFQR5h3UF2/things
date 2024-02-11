import argparse
import logging
import os
import sys

from shishifubing.leetcode.submissions_downloader import SubmissionsDownloader
from shishifubing.leetcode.submissions_generator import SubmissionsGenerator
from shishifubing.leetcode.submissions_repo import SubmissionsRepo
from shishifubing.leetcode.types import Action, Config, LeetcodeException

logger = logging.getLogger(__name__)


def cli() -> None:
    logging.basicConfig(level=logging.INFO)
    main(sys.argv[1:], os.environ)


def main(args: list[str], env: dict[str, str] | os._Environ) -> None:
    config = _parse_args(args, env)
    downloader = SubmissionsDownloader(config=config)
    repo = SubmissionsRepo(config=config)
    generator = SubmissionsGenerator(config=config)
    match config.action:
        case Action.download:
            print(downloader.download(config.offset, config.limit).model_dump_json())
        case Action.update:
            _update(downloader, repo, config)
        case Action.generate:
            generator.generate_submissions(repo.read_submission_file())
        case _:
            raise LeetcodeException(f"invalid action: {config.action}")


def _update(
    downloader: SubmissionsDownloader, repo: SubmissionsRepo, config: Config
) -> None:
    offset = config.offset
    limit = config.limit
    while limit > 0:
        count = min(limit, 20)
        submissions = downloader.download(offset, count)
        repo.update_submissions_file(submissions)
        offset += count
        limit -= count


def _parse_args(args: list[str], env: dict[str, str] | os._Environ) -> Config:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action", choices=[el.value for el in Action], help="what action to take"
    )
    parser.add_argument(
        "-b",
        "--base-url",
        dest="base_url",
        default="https://leetcode.com",
        help="Leetcode base url with protocol (default: https://leetcode.com)",
    )
    parser.add_argument(
        "-s",
        "--session",
        dest="session",
        default=env.get("LEETCODE_SESSION"),
        help="Session cookie to download submissions (default: ${LEETCODE_SESSION})",
    )
    parser.add_argument(
        "-f",
        "--submissions-file",
        dest="submissions_file",
        default="submissions.json",
        help="JSON file to write submissions to (default: submissions.json)",
    )
    parser.add_argument(
        "-d",
        "--submissions-dir",
        dest="submissions_dir",
        default="submissions",
        help="Directory to generate submissions in (default: submissions)",
    )
    parser.add_argument(
        "-o",
        "--offset",
        dest="offset",
        default=0,
        help="Offset of submissions downloads (default: 0)",
    )
    parser.add_argument(
        "-l",
        "--limit",
        dest="limit",
        default=20,
        help="Limit of submission downloads (default: 20)",
    )

    return Config(**vars(parser.parse_args(args)))
