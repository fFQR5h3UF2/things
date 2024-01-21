include ../make/common.mk

.PHONY: remove-bashrc

install: install-stow | remove-bashrc-file
build: build-stow
test: test-stow

remove-bashrc-file:
	if [ -f "${HOME}/.bashrc" ]; then rm "${HOME}/.bashrc"; fi
