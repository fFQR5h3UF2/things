nvim: nvim/install ## Run nvim/install
nvim/install: nvim/install-stow ## Install stow package
nvim/build: nvim/build-stow ## Build stow package
nvim/test: nvim/test-stow ## Test stow package
nvim/clean: nvim/clean-stow ## Clean stow package

.PHONY: nvim/sync
nvim/sync: ## Update Lazy packages
	nvim --headless "+Lazy! sync" +qa
