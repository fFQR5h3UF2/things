include ../make/common.mk

.PHONY: sync

install: install-stow
build: build-stow
test: test-stow
update: sync
sync: install
	nvim --headless "+Lazy! sync" +qa
