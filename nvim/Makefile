.PHONY: install sync

install:
	stow --restow --no-folding --target="${HOME}" src

sync:
	nvim --headless "+Lazy! sync" +qa
