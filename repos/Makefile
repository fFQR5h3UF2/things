repos: repos/apply ## Run repos/apply

.PHONY: repos/apply
repos/apply: ## Apply
	terraform apply

.PHONY: repos/clean-tf
repos/clean-tf: ## Clean state
	mapfile -t args < <(terraform state list); \
	terraform state rm "$${args[@]}"

.PHONY: repos/docs
repos/docs: ## Update terraform docs
	terraform-docs markdown table --recursive --output-file README.md .

.PHONY: repos/import
repos/import: ## Run import script
	./scripts/import.sh

.PHONY: repos/init
repos/init: ## Terraform init
	terraform init -reconfigure -backend-config="main.s3.tfbackend"

.PHONY: repos/list
repos/list: ## Terraform state list
	terraform state list
