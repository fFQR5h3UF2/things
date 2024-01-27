include ../make/common.mk

install: install-stow-package install-tmux
build: build-stow-package
test: test-stow-package

install-tmux: setup-poetry-no-root
	$(call ansible-install,tmux,tmux)
.PHONY: install-tmux
