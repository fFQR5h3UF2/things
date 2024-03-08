import json
import os
import pathlib
import sys
from typing import Any

import jsonschema

from pkg.gitlab_pipeline_generator.types import Pipeline


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
        pipeline_dump = pipeline.dump()
        pipeline_dict = {
            **pipeline_dump.get("meta", {}),
            **pipeline_dump.get("jobs", {}),
        }
        self.validator.validate(pipeline_dict)
        return pipeline_dict

    def render_string(self, pipeline: Pipeline) -> str:
        return json.dumps(self.render(pipeline), indent=4)

    def render_to_file(self, pipeline: Pipeline, path: pathlib.Path) -> None:
        content = self.render_string(pipeline)
        with open(path, "w") as file:
            file.write(content)


if __name__ == "__main__":
    print(sys.version)
