include ../make/common.mk

install: install-stow install-tmux
build: build-stow
test: test-stow

install-tmux: setup-poetry-no-root
	$(ANSIBLE_CMD) ./playbook_tmux.yml
.PHONY: install-tmux
