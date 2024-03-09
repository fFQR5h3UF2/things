import contextlib
import json
import sys
from typing import Any, ContextManager

import jsonschema
import pytest

from pkg.gitlab_pipeline_generator.main import Renderer, Validator
from pkg.gitlab_pipeline_generator.types import (
    Artifacts,
    ArtifactsWhen,
    Cache,
    Job,
    JobWhen,
    Pipeline,
    PredefinedVar,
    Retry,
    RetryWhen,
    Rule,
    Trigger,
    TriggerInclude,
    Workflow,
)


@pytest.fixture
def validator() -> Validator:
    return Validator()


@pytest.fixture
def renderer(validator: Validator) -> Renderer:
    return Renderer(validator)


def test_renderer_should_render_pipeline_with_extends(
    renderer: Renderer,
) -> None:
    base_job = Job(
        name=".job:base",
        stage="jobs",
        artifacts=Artifacts(expire_in="1 day", when=ArtifactsWhen.ALWAYS),
        cache=Cache(),
        interruptible=True,
        script=["base-job"],
        variables={
            "var_base": "var_base",
            "job_id": f"${PredefinedVar.CI_JOB_ID}",
        },
        retry=Retry(
            max=1,
            when=[
                RetryWhen.DATA_INTEGRITY_FAILURE,
                RetryWhen.API_FAILURE,
                RetryWhen.UNKNOWN_FAILURE,
            ],
        ),
    )
    job_1 = Job(
        name="job-1",
        extends=[base_job],
        script=["job-1"],
        artifacts=Artifacts(paths=["./out/upload"], expire_in="30 minutes"),
        variables={"var_1": "var_1", "var_base": "var_1"},
    )
    job_2 = Job(
        name="job-2",
        extends=[base_job],
        script=["job-2"],
        interruptible=False,
        resource_group="job-2",
    )
    pipeline = Pipeline(stages=["jobs"], jobs=[job_1, job_2])
    assert renderer.render(pipeline) == {
        "stages": ["jobs"],
        "job-1": {
            "stage": "jobs",
            "artifacts": {
                "expire_in": "30 minutes",
                "when": "always",
                "paths": ["./out/upload"],
            },
            "variables": {
                "var_1": "var_1",
                "var_base": "var_1",
                "job_id": "$CI_JOB_ID",
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
            "variables": {
                "var_base": "var_base",
                "job_id": "$CI_JOB_ID",
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
        (Pipeline(jobs=[]), contextlib.nullcontext()),
        (
            Pipeline(jobs=[Job(name="empty-script", script=[])]),
            pytest.raises(jsonschema.ValidationError),
        ),
        (
            Pipeline(
                jobs=[
                    Job(
                        name="trigger-with-script",
                        script=[],
                        trigger=Trigger(
                            include=[TriggerInclude(local="path.yml")]
                        ),
                    )
                ]
            ),
            pytest.raises(jsonschema.ValidationError),
        ),
        (
            Pipeline(
                jobs=[
                    Job(
                        name="trigger-without-script-invalid-path",
                        trigger=Trigger(
                            include=[
                                TriggerInclude(local="path-without-extension")
                            ]
                        ),
                    )
                ]
            ),
            pytest.raises(jsonschema.ValidationError),
        ),
        (
            Pipeline(
                jobs=[
                    Job(
                        name="trigger-without-script-correct-path",
                        trigger=Trigger(
                            include=[TriggerInclude(local="path.yml")]
                        ),
                    )
                ]
            ),
            contextlib.nullcontext(),
        ),
        (
            Pipeline(
                workflow=Workflow(
                    name=f"${PredefinedVar.CI_COMMIT_TITLE}",
                    rules=[
                        Rule(
                            if_=f"${PredefinedVar.CI_PIPELINE_SOURCE} != 'push' && ${PredefinedVar.CI_OPEN_MERGE_REQUESTS}",
                            when=JobWhen.NEVER,
                        ),
                        Rule(
                            when=JobWhen.ALWAYS,
                        ),
                    ],
                ),
            ),
            contextlib.nullcontext(),
        ),
        (
            Pipeline(jobs=[Job(name="non-empty-script", script=["check"])]),
            contextlib.nullcontext(),
        ),
        (
            Pipeline(
                extends=[Pipeline(extends=[Pipeline(stages=["stage-1"])])],
                jobs=[Job(name="non-empty-script", script=["check"])],
            ),
            contextlib.nullcontext(),
        ),
        (
            Pipeline(
                extends=[Pipeline(jobs=[Job(name="non-empty-script")])],
                jobs=[Job(name="non-empty-script", script=["check"])],
            ),
            contextlib.nullcontext(),
        ),
        (
            Pipeline(
                extends=[
                    Pipeline(
                        jobs=[Job(name="non-empty-script", script=["check"])]
                    )
                ],
            ),
            contextlib.nullcontext(),
        ),
        (None, pytest.raises(AttributeError)),
    ],
)
def test_renderer_should_render_without_extends(
    renderer: Renderer, pipeline: Pipeline, expectation: ContextManager
) -> None:
    with expectation:
        renderer.render(pipeline)


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
def test_validator_should_validate_pipeline_as_dict(
    validator: Validator, pipeline: dict[str, Any], expectation: ContextManager
) -> None:
    with expectation:
        validator.validate(pipeline)


@pytest.mark.parametrize(
    "pipeline,should_render,expectation",
    [
        (Pipeline(), "{}", contextlib.nullcontext()),
        (
            Pipeline(workflow=Workflow(name="check")),
            json.dumps({"workflow": {"name": "check"}}, indent=4),
            contextlib.nullcontext(),
        ),
        (None, "", pytest.raises(AttributeError)),
    ],
)
def test_renderer_should_render_string(
    renderer: Renderer,
    pipeline: Pipeline,
    should_render: str,
    expectation: ContextManager,
) -> None:
    with expectation:
        assert renderer.render_string(pipeline) == should_render


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-vv", *sys.argv[1:]]))
