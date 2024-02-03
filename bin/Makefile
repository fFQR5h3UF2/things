bin_packages_pipx = $(shell cat ./bin/packages-pipx.txt)
bin_nvm_version = v0.39.7

bin: bin/install
bin/install: bin/install-stow bin/install-pipx bin/install-npm
bin/build: bin/build-stow
bin/test: bin/test-stow
bin/clean: bin/clean-stow bin/clean-pipx bin/clean-npm
bin/setup: shell

bin_pipx_targets = $(bin_packages_pipx:%=bin/install-pipx-%)
.PHONY: bin/install-pipx $(bin_pipx_targets)
bin/install-pipx: $(bin_pipx_targets)
$(bin_pipx_targets): %: ${OUT_TRACKER_DIR}/%
$(bin_pipx_targets:%=${OUT_TRACKER_DIR}/%): ${OUT_TRACKER_DIR}/bin/install-pipx-%:
	poetry run pipx install "${*}"
	touch "${@}"

.PHONY: bin/install-npm
bin/install-npm: NVM_DIR = ~/.config/nvm
bin/install-npm: %: ${OUT_TRACKER_DIR}/%
${OUT_TRACKER_DIR}/bin/install-npm: ${OUT_TRACKER_DIR}/bin/install-nvm-${bin_nvm_version}
	. "${NVM_DIR}/nvm.sh" && nvm install node
	touch "${@}"
${OUT_TRACKER_DIR}/bin/install-nvm-${bin_nvm_version}: | ${NVM_DIR}
	curl -o- "https://raw.githubusercontent.com/nvm-sh/nvm/${bin_nvm_version}/install.sh" \
		| PROFILE=/dev/null bash
	touch "${@}"
${NVM_DIR}:
	mkdir -p "${@}"
.PHONY: bin/clean-npm bin/clean-nvm
bin/clean-npm: bin/clean-nvm
	-rm -rf "${OUT_TRACKER_DIR}/bin/install-npm"
bin/clean-nvm:
	-rm -rf "${NVM_DIR}"
	-rm -rf "${OUT_TRACKER_DIR}/bin/install-nvm"

bin_pipx_clean_targets = $(bin_packages_pipx:%=bin/clean-pipx-%)
.PHONY: bin/clean-pipx $(bin_pipx_clean_targets)
bin/clean-pipx: $(bin_pipx_clean_targets)
$(bin_pipx_clean_targets): bin/clean-pipx-%:
	-poetry run pipx uninstall "${*}"
