tmux/install: tmux/install-stow tmux/install-tmux
tmux/build: tmux/build-stow
tmux/test: tmux/test-stow
tmux/clean: tmux/clean-stow

.PHONY: tmux/install-tmux
tmux/install-tmux: init/ansible-galaxy
	$(call ansible-install,tmux,tmux)
