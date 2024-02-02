nvim: nvim/install
nvim/install: nvim/install-stow
nvim/build: nvim/build-stow
nvim/test: nvim/test-stow
nvim/clean: nvim/clean-stow

.PHONY: nvim/sync
nvim/sync:
	nvim --headless "+Lazy! sync" +qa
