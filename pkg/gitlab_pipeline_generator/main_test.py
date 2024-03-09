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


def test_expand_extends(renderer: Renderer) -> None:
    job_1 = Job(name="job-1", script=["job-1"])
    job_2 = Job(
        name="job-2", extends=[job_1], interruptible=True, script=["job-2"]
    )
    job_3 = Job(name="job-3", extends=[job_2], script=["job-3"])
    expanded = renderer.expand_extends(job_3).dump()
    must_equal = job_3.dump()
    must_equal.update(
        {
            "script": ["job-1", "job-2", "job-3"],
            "interruptible": True,
            "extends": [],
        }
    )
    assert expanded == must_equal


def test_pipeline(renderer: Renderer) -> None:
    base_job = Job(
        name=".job:base",
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
    job_1 = Job(
        name="job-1",
        extends=[base_job],
        script=["job-1"],
        artifacts=Job.Artifacts(paths=["./out/upload"], expire_in="30 minutes"),
    )
    job_2 = Job(
        name="job-2",
        extends=[base_job],
        script=["job-2"],
        interruptible=False,
        resource_group="job-2",
    )
    pipeline = Pipeline(meta=Meta(stages=["jobs"]), jobs=[job_1, job_2])
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
        (Pipeline(jobs=[]), contextlib.nullcontext()),
        (
            Pipeline(jobs=[Job(name="empty-script", script=[])]),
            pytest.raises(jsonschema.ValidationError),
        ),
        (
            Pipeline(jobs=[Job(name="non-empty-script", script=["check"])]),
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
