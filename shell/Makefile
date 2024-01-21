include ../make/common.mk

.PHONY: remove-bashrc

install: install-stow
build: build-stow
test: test-stow

install-stow: | remove-bashrc-file
remove-bashrc-file:
	if [ -f "${HOME}/.bashrc" ]; then rm "${HOME}/.bashrc"; fi
