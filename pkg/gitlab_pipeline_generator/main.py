import json
import os
import pathlib
from typing import Any, TypeVar, Union

import deepmerge
import jsonschema

from pkg.gitlab_pipeline_generator.types import Job, Pipeline

T = TypeVar("T", bound=Union[Job, Pipeline])


def load_validator_schema() -> dict[str, Any]:
    schema_path = (
        pathlib.Path(os.path.dirname(os.path.abspath(__file__))) / "schema.json"
    )
    with open(schema_path, "r") as file:
        return json.loads(file.read())


class Validator:
    def __init__(self, schema: dict[str, Any]) -> None:
        self.schema = schema

    def validate(self, pipeline: dict[str, Any]) -> None:
        jsonschema.validate(instance=pipeline, schema=self.schema)


class Renderer:
    def __init__(self, validator: Validator) -> None:
        self.validator = validator

    def render(self, pipeline: Pipeline) -> dict[str, Any]:
        pipeline = self._expand_extends(pipeline)
        res = pipeline.dump(include=["meta"]).get("meta", {})
        for job in pipeline.jobs:
            job = self._expand_extends(job)
            res[job.name] = job.dump(exclude=["name", "extends"])
        self.validator.validate(res)
        return res

    def render_string(self, pipeline: Pipeline) -> str:
        return json.dumps(self.render(pipeline), indent=4)

    def render_to_file(self, pipeline: Pipeline, path: pathlib.Path) -> None:
        content = self.render_string(pipeline)
        with open(path, "w") as file:
            file.write(content)

    def _expand_extends(self, model: T) -> T:
        if not model.extends:
            return model
        res = self._expand_extends_dict(model.dump())
        if isinstance(model, Pipeline):
            jobs = res.get("jobs", [])
            for i in range(len(jobs)):
                jobs[i] = self._expand_extends_dict(jobs[i])
            res["jobs"] = jobs
        return model.model_validate(res)

    def _expand_extends_dict(self, model: dict[str, Any]) -> dict[str, Any]:
        extends = model.get("extends", [])
        if not extends:
            return model
        res = {}
        for model_extends in extends:
            expanded = self._expand_extends_dict(model_extends)
            res = deepmerge.always_merger.merge(res, expanded)
        res = deepmerge.always_merger.merge(res, model)
        res["extends"] = []
        return res
