tmux: tmux/install ## Run tmux/install
tmux/install: tmux/install-stow tmux/install-tmux ## Install tmux, install stow package
tmux/build: tmux/build-stow ## Build stow package
tmux/test: tmux/test-stow ## Test stow package
tmux/clean: tmux/clean-stow ## Clean stow package

.PHONY: tmux/install-tmux
tmux/install-tmux: init/ansible-galaxy ## Install tmux
	$(call ansible-install,tmux,tmux)
