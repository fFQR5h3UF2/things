dotfiles/tmux: dotfiles/tmux/install ## Run dotfiles/tmux/install
dotfiles/tmux/install: dotfiles/tmux/install-stow dotfiles/tmux/install-dotfiles/tmux ## Install dotfiles/tmux, install stow package
dotfiles/tmux/build: dotfiles/tmux/build-stow ## Build stow package
dotfiles/tmux/test: dotfiles/tmux/test-stow ## Test stow package
dotfiles/tmux/clean: dotfiles/tmux/clean-stow ## Clean stow package

.PHONY: dotfiles/tmux/install-dotfiles/tmux
dotfiles/tmux/install-dotfiles/tmux: init/ansible-galaxy ## Install dotfiles/tmux
	$(call ansible-install,dotfiles/tmux,dotfiles/tmux)
