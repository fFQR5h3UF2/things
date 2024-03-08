import contextlib
import sys
from typing import Any, ContextManager

import jsonschema
import pytest

from pkg.gitlab_pipeline_generator.main import (
    Renderer,
    Validator,
    load_validator_schema,
)
from pkg.gitlab_pipeline_generator.types import Job, Meta, Pipeline


@pytest.fixture
def validator() -> Validator:
    return Validator(load_validator_schema())


@pytest.fixture
def renderer(validator: Validator) -> Renderer:
    return Renderer(validator)


def test_extend(renderer: Renderer) -> None:
    base_job = Job(
        stage="jobs",
        artifacts=Job.Artifacts(
            expire_in="1 day", when=Job.Artifacts.When.always
        ),
        cache=Job.Cache(),
        interruptible=True,
        script=["base-job"],
        retry=Job.Retry(
            max=1,
            when=[
                Job.RetryWhen.data_integrity_failure,
                Job.RetryWhen.api_failure,
                Job.RetryWhen.unknown_failure,
            ],
        ),
    )
    job_1 = base_job.extend(
        Job(
            script=["job-1"],
            artifacts=Job.Artifacts(
                paths=["./out/upload"], expire_in="30 minutes"
            ),
        ),
    )
    job_2 = base_job.extend(
        Job(script=["job-2"], interruptible=False, resource_group="job-2"),
    )
    pipeline = Pipeline(
        meta=Meta(stages=["jobs"]), jobs={"job-1": job_1, "job-2": job_2}
    )
    assert renderer.render(pipeline) == {
        "stages": ["jobs"],
        "job-1": {
            "stage": "jobs",
            "artifacts": {
                "expire_in": "30 minutes",
                "when": "always",
                "paths": ["./out/upload"],
            },
            "cache": {},
            "interruptible": True,
            "script": ["base-job", "job-1"],
            "retry": {
                "max": 1,
                "when": [
                    "data_integrity_failure",
                    "api_failure",
                    "unknown_failure",
                ],
            },
        },
        "job-2": {
            "stage": "jobs",
            "artifacts": {
                "expire_in": "1 day",
                "when": "always",
            },
            "cache": {},
            "interruptible": False,
            "script": ["base-job", "job-2"],
            "retry": {
                "max": 1,
                "when": [
                    "data_integrity_failure",
                    "api_failure",
                    "unknown_failure",
                ],
            },
            "resource_group": "job-2",
        },
    }


@pytest.mark.parametrize(
    "pipeline,expectation",
    [
        ({}, contextlib.nullcontext()),
        (
            {"job-empty-script": {"script": []}},
            pytest.raises(jsonschema.ValidationError),
        ),
        (
            {"job-non-empty-script": {"script": ["lines"]}},
            contextlib.nullcontext(),
        ),
        (None, pytest.raises(jsonschema.ValidationError)),
    ],
)
def test_validator(
    validator: Validator, pipeline: dict[str, Any], expectation: ContextManager
) -> None:
    with expectation:
        validator.validate(pipeline)


@pytest.mark.parametrize(
    "pipeline,expectation",
    [
        (Pipeline(jobs={}), contextlib.nullcontext()),
        (
            Pipeline(jobs={"job-empty-script": Job(script=[])}),
            pytest.raises(jsonschema.ValidationError),
        ),
        (
            Pipeline(jobs={"job-non-empty-script": Job(script=["check"])}),
            contextlib.nullcontext(),
        ),
        (None, pytest.raises(AttributeError)),
    ],
)
def test_renderer(
    renderer: Renderer, pipeline: Pipeline, expectation: ContextManager
) -> None:
    with expectation:
        renderer.render(pipeline)


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-vv", *sys.argv[1:]]))
