include ../make/common.mk

apply ::
	terraform apply

clean: clean-tf

clean-tf:
	mapfile -t args < <(terraform state list); \
	terraform state rm "$${args[@]}"

docs ::
	terraform-docs markdown table --recursive --output-file README.md .

import ::
	./scripts/import.sh

init ::
	terraform init -reconfigure -backend-config="main.s3.tfbackend"

list ::
	terraform state list
