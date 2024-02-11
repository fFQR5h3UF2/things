import dataclasses
import json
import logging

from shishifubing.leetcode.types import Config, Submissions, SubmissionsResponse

logger = logging.getLogger(__name__)


class SubmissionsRepo:

    def __init__(self, config: Config) -> None:
        self.config = config

    def update_submissions_file(self, response: SubmissionsResponse) -> None:
        new_submissions = self._response_to_submissions(response)
        cur_submissions = self.read_submission_file()
        updated_submissions = self._combine_submissions(
            cur_submissions, new_submissions
        )
        self._write_submission_file(updated_submissions)

    def read_submission_file(self) -> Submissions:
        with open(self.config.submissions_file, "r") as file:
            return Submissions(**json.loads(file.read()))

    def _write_submission_file(self, submissions: Submissions) -> None:
        with open(self.config.submissions_file, "w") as file:
            file.write(json.dumps(dataclasses.asdict(submissions)))

    def _combine_submissions(
        self, cur_submissions: Submissions, new_submissions: Submissions
    ) -> Submissions:
        updated = list(cur_submissions.submissions)
        ids = set(submission.id for submission in cur_submissions.submissions)
        for submission in new_submissions.submissions:
            if submission.id not in ids:
                updated.append(submission)
        return Submissions(submissions=tuple(updated))

    def _response_to_submissions(self, response: SubmissionsResponse) -> Submissions:
        return Submissions(submissions=response.submissions_dump)
