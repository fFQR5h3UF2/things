BIN_DIR = ${PACKAGE_DIR}/dotfiles/bin
BIN_PACKAGES_PIPX = $(shell cat "${BIN_DIR}/packages-pipx.txt")
BIN_NVM_VERSION = v0.39.7

bin: bin/install ## Run bin/install
bin/install: bin/install-stow bin/install-pipx bin/install-npm ## Install pipx packages, npm, and stow package
bin/build: bin/build-stow ## Build stow package
bin/test: bin/test-stow ## Test stow package
bin/clean: bin/clean-stow bin/clean-pipx bin/clean-npm ## Clean stow package, clean pipx packages, clean npm

bin_pipx_targets = $(BIN_PACKAGES_PIPX:%=bin/install-pipx-%)
.PHONY: bin/install-pipx $(bin_pipx_targets)
bin/install-pipx: $(bin_pipx_targets) ## Install pipx packages
$(bin_pipx_targets): %: ${OUT_TRACKER_DIR}/%
$(bin_pipx_targets:%=${OUT_TRACKER_DIR}/%): ${OUT_TRACKER_DIR}/bin/install-pipx-%:
	poetry run pipx install "${*}"
	touch "${@}"

.PHONY: bin/install-npm
bin/install-npm: NVM_DIR = ${HOME}/.config/nvm
bin/install-npm: %: ${OUT_TRACKER_DIR}/% ## Install npm
bin/install-nvm: ${OUT_TRACKER_DIR}/bin/install-nvm-${BIN_NVM_VERSION} ## Install nvm in ${NVM_DIR}
${OUT_TRACKER_DIR}/bin/install-npm: ${OUT_TRACKER_DIR}/bin/install-nvm-${BIN_NVM_VERSION}
	. "${NVM_DIR}/nvm.sh" && nvm install node
	touch "${@}"
${OUT_TRACKER_DIR}/bin/install-nvm-${BIN_NVM_VERSION}: | ${NVM_DIR}
	curl -o- "https://raw.githubusercontent.com/nvm-sh/nvm/${BIN_NVM_VERSION}/install.sh" \
		| PROFILE=/dev/null bash
	touch "${@}"
${NVM_DIR}:
	mkdir -p "${@}"
.PHONY: bin/clean-npm bin/clean-nvm
bin/clean-npm: bin/clean-nvm ## Clean npm install tracker
	-rm -rf "${OUT_TRACKER_DIR}/bin/install-npm"
bin/clean-nvm: ## Clean ${NVM_DIR} and nvm install tracker
	-rm -rf "${NVM_DIR}"
	-rm -rf "${OUT_TRACKER_DIR}/bin/install-nvm"

bin_pipx_clean_targets = $(BIN_PACKAGES_PIPX:%=bin/clean-pipx-%)
.PHONY: bin/clean-pipx $(bin_pipx_clean_targets)
bin/clean-pipx: $(bin_pipx_clean_targets) ## Clean pipx packages
$(bin_pipx_clean_targets): bin/clean-pipx-%:
	-poetry run pipx uninstall "${*}"
