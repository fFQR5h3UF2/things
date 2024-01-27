include ../make/common.mk

.PHONY: remove-bashrc

install: install-stow-package
build: build-stow-package
test: test-stow-package

install-stow-package: remove-bashrc-file

remove-bashrc-file:
	if [ -f "${HOME}/.bashrc" ]; then rm "${HOME}/.bashrc"; fi
