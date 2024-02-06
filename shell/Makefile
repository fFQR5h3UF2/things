shell: shell/install ## Run shell/install
shell/install: shell/install-stow ## Install stow package
shell/build: shell/build-stow ## Build stow package
shell/clean: shell/clean-stow ## Clean stow package
shell/test: shell/test-stow ## Test stow package

.PHONY: shell/remove-bashrc
shell/remove-bashrc: ## Disable current .bashrc if it is a file
	if [ -f ~/.bashrc ] && [ ! -L ~/.bashrc ]; then mv ~/.bashrc ~/.bashrc.disabled; fi
