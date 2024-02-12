import json
import logging
import os

from shishifubing.leetcode.types import Config, Submissions, SubmissionsResponse

logger = logging.getLogger(__name__)


class SubmissionsRepo:

    def __init__(self, config: Config) -> None:
        self.config = config

    def update_submissions(self, response: SubmissionsResponse) -> None:
        new_submissions = self._response_to_submissions(response)
        cur_submissions = self.submissions()
        updated_submissions = self._combine_submissions(
            cur_submissions, new_submissions
        )
        self._write_submission_file(updated_submissions)

    def submissions(self) -> Submissions:
        with open(self.config.submissions_file, "r") as file:
            return Submissions.model_validate_json(file.read())

    def _write_submission_file(self, submissions: Submissions) -> None:
        path = self.config.submissions_file
        logger.info(f"writing {len(submissions.submissions)} submissions to {path}")
        with open(path, "w") as file:
            file.write(submissions.model_dump_json())

    def _combine_submissions(
        self, cur_submissions: Submissions, new_submissions: Submissions
    ) -> Submissions:
        cur_ids = set(submission.id for submission in cur_submissions.submissions)
        need_to_add = filter(lambda s: s.id not in cur_ids, new_submissions.submissions)
        return Submissions(submissions=cur_submissions.submissions + tuple(need_to_add))

    def _response_to_submissions(self, response: SubmissionsResponse) -> Submissions:
        return Submissions(submissions=response.submissions_dump)
