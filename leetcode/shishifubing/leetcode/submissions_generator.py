import json
import logging
from pathlib import Path

from shishifubing.leetcode.types import Config, Submission, SubmissionFile, Submissions

logger = logging.getLogger(__name__)
extensions = {"python3": "py", "golang": "go", "cpp": "cpp", "java": "java"}
comments = {"python3": "#", "golang": "//", "cpp": "//", "java": "//"}
headers = {
    "python3": "",
    "golang": "package submissions",
    "cpp": "",
    "java": "com.shishifubing.dotfiles.submissions",
}


class SubmissionsGenerator:
    def __init__(self, config: Config) -> None:
        self.config = config

    def _submission_path(self, submission: Submission) -> Path:
        extension = extensions[submission.lang]
        file_name = "-".join(
            (
                str(submission.question_id).rjust(5, "0"),
                submission.title_slug,
                str(submission.id),
            )
        )
        return Path(self.config.submissions_dir) / f"{file_name}.{extension}"

    def _submission_content(self, submission: Submission) -> str:
        comment = comments[submission.lang]
        header = headers[submission.lang]
        lines = [
            f"{comment} Submission title: {submission.title}",
            f"{comment} Submission url  : {self.config.base_url}/problems/{submission.title_slug}/description/",
            f"{comment} Submission url  : {self.config.base_url}{submission.url}",
            f"{comment} Submission json : {submission.model_dump_json()}",
            header,
            *(
                line.rstrip()
                for line in submission.code.split("\n")
                # gofmt fix for 691642817 and 691652127
                if submission.lang != "golang" or not line.startswith("package ")
            ),
        ]
        length = len(lines)
        for i in reversed(range(length)):
            line = lines[i]
            if line and not line.isspace():
                break
            lines.pop()
        if lines[-1][-1] != "\n":
            lines[-1] += "\n"
        return "\n".join(lines)

    def prepare_submission_files(
        self, submissions: Submissions
    ) -> list[SubmissionFile]:
        files = []
        for submission in submissions.submissions:
            if submission.status_display != "Accepted":
                continue
            files.append(
                SubmissionFile(
                    submission=submission,
                    path=self._submission_path(submission),
                    text=self._submission_content(submission),
                )
            )
        return files

    def generate_submissions(self, submissions: Submissions) -> None:
        for submission in self.prepare_submission_files(submissions):
            with open(submission.path, "w") as file:
                file.write(submission.text)
