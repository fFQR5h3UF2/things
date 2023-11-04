all-links :: git home nvim firefox vscode

git ::
	stow --target="$${HOME}" git

home ::
	stow --target="$${HOME}" home

nvim ::
	stow --target="$${HOME}" nvim

firefox ::
	for profile in $(wildcard $${HOME}/.mozilla/firefox/*.default-release-*); do \
		stow --target="$${profile}" firefox; \
	done;

vscode ::
	for dir in "Code - OSS" "Code" "VSCodium"; do \
		stow --target="$${HOME}/.config/$${dir}" vscode; \
	done;

setup ::
	./scripts/setup_packages.sh
