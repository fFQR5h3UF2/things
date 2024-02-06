dotfiles/nvim: dotfiles/nvim/install ## Run dotfiles/nvim/install
dotfiles/nvim/install: dotfiles/nvim/install-stow ## Install stow package
dotfiles/nvim/build: dotfiles/nvim/build-stow ## Build stow package
dotfiles/nvim/test: dotfiles/nvim/test-stow ## Test stow package
dotfiles/nvim/clean: dotfiles/nvim/clean-stow ## Clean stow package

.PHONY: dotfiles/nvim/sync
dotfiles/nvim/sync: ## Update Lazy packages
	nvim --headless "+Lazy! sync" +qa
