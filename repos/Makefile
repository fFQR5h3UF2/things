repos: repos/apply

.PHONY: repos/apply
repos/apply:
	terraform apply

.PHONY: repos/clean-tf
repos/clean-tf:
	mapfile -t args < <(terraform state list); \
	terraform state rm "$${args[@]}"

.PHONY: repos/docs
repos/docs:
	terraform-docs markdown table --recursive --output-file README.md .

.PHONY: repos/import
repos/import:
	./scripts/import.sh

.PHONY: repos/init
repos/init:
	terraform init -reconfigure -backend-config="main.s3.tfbackend"

.PHONY: repos/list
repos/list:
	terraform state list
