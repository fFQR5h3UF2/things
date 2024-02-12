import enum
import pathlib
from typing import Optional

import pydantic


class LeetcodeException(Exception):
    pass


class Action(enum.Enum):
    download = "download"
    generate = "generate"
    update = "update"

    def __str__(self):
        return self.value


class Config(pydantic.BaseModel):
    base_url: str
    submissions_file: pathlib.Path
    submissions_dir: pathlib.Path
    session: str
    action: Action
    offset: int
    limit: int


class Submission(pydantic.BaseModel):
    id: int
    status_display: str
    lang: str
    question_id: int
    title_slug: str
    code: str
    title: str
    url: str
    lang_name: str
    time: str
    timestamp: int
    status: int
    runtime: str
    is_pending: str
    memory: str
    compare_result: Optional[str]
    has_notes: bool
    flag_type: int


class SubmissionFile(pydantic.BaseModel):
    submission: Submission
    path: pathlib.Path
    text: str


class SubmissionsResponse(pydantic.BaseModel):
    submissions_dump: tuple[Submission, ...]


class Submissions(pydantic.BaseModel):
    submissions: tuple[Submission, ...]
