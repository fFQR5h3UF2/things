import json
import os
import pathlib
from typing import Any, Optional

import deepmerge
import jsonschema

from pkg.gitlab_pipeline_generator.types import Pipeline


class Validator:
    def __init__(self, schema: Optional[dict[str, Any]] = None) -> None:
        self.schema = schema or self.load_default_schema()

    def validate(self, pipeline: dict[str, Any]) -> None:
        jsonschema.validate(instance=pipeline, schema=self.schema)

    @staticmethod
    def load_default_schema() -> dict[str, Any]:
        dir = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))
        schema_path = dir / "schema.json"
        with open(schema_path, "r") as file:
            return json.loads(file.read())


class Renderer:
    def __init__(self, validator: Validator) -> None:
        self.validator = validator

    def render(self, pipeline: Pipeline) -> dict[str, Any]:
        pipeline = self._apply_extends(pipeline)
        res = pipeline.dump(exclude=["jobs", "extends"])
        for job in pipeline.jobs:
            if job.name in res:
                raise ValueError(
                    "name collision: pipeline already has a job with name "
                    f"'{job.name}'"
                )
            res[job.name] = job.dump(exclude=["name", "extends"])
        self.validator.validate(res)
        return res

    def render_string(self, pipeline: Pipeline) -> str:
        return json.dumps(self.render(pipeline), indent=4)

    def render_file(self, pipeline: Pipeline, path: pathlib.Path) -> None:
        content = self.render_string(pipeline)
        with open(path, "w") as file:
            file.write(content)

    def _apply_extends(self, model: Pipeline) -> Pipeline:
        res = self._apply_extends_dict(model.dump(exclude=["jobs"]))
        res["jobs"] = [
            self._apply_extends_dict(job.dump()) for job in model.jobs
        ]
        return model.model_validate(res)

    def _apply_extends_dict(self, model: dict[str, Any]) -> dict[str, Any]:
        extends = model.get("extends", [])
        if not extends:
            return model
        res = {}
        for model_extends in extends:
            applied = self._apply_extends_dict(model_extends)
            res = deepmerge.always_merger.merge(res, applied)
        res = deepmerge.always_merger.merge(res, model)
        return res
