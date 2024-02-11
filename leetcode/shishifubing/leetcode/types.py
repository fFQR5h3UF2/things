import enum
import pathlib

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
    timestamp: str
    status: str
    runtime: str
    is_pending: str
    memory: str
    compare_result: str
    has_notes: str
    flag_type: str


class SubmissionFile(pydantic.BaseModel):
    submission: Submission
    path: pathlib.Path
    text: str


class SubmissionsResponse(pydantic.BaseModel):
    submissions_dump: tuple[Submission, ...]


class Submissions(pydantic.BaseModel):
    submissions: tuple[Submission, ...]
