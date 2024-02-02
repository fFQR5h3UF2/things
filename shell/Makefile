shell: shell/install
shell/install: shell/install-stow
shell/build: shell/build-stow
shell/clean: shell/clean-stow
shell/test: shell/test-stow

shell/install-stow: shell/remove-bashrc

.PHONY: shell/remove-bashrc
shell/remove-bashrc:
	if [ -f ~/.bashrc ] && [ ! -L ~/.bashrc ]; then mv ~/.bashrc ~/.bashrc.disabled; fi
