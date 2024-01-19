TARGET = $(HOME)

.PHONY: install clean stow setup

install: stow
	stow --restow --no-folding --target="${TARGET}" stow

clean:
	stow --delete --no-folding --target="${TARGET}" stow
	rm -r stow

setup:
	mkdir -p stow/.local/bin/

stow: stow/.local/bin/readme-tree

stow/.local/bin/readme-tree: setup
	ln --relative --symbolic --force ./scripts/readme-tree.sh "${@}"
