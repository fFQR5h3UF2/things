firefox_dir = .mozilla/firefox
firefox_stow_out_dir = ${OUT_STOW_DIR}/firefox/${firefox_dir}
firefox_profiles = $(notdir $(wildcard ${HOME}/${firefox_dir}/*.default-release-*))
firefox_targets = $(firefox_profiles:%=firefox/build-%)
firefox_out_dirs = $(firefox_profiles:%=${firefox_stow_out_dir}/%)

firefox: firefox/install ## Run firefox/install
firefox/install: firefox/install-stow ## Install stow package
firefox/setup: | $(firefox_out_dirs) ## Prepare directories
firefox/build: $(firefox_targets) ## Build stow package
firefox/test: firefox/test-stow ## Test stow package
firefox/clean: firefox/clean-stow ## Clean stow package

.PHONY: $(firefox_targets)
$(firefox_targets): firefox/build-%:
	$(STOW_CMD) --target "${firefox_stow_out_dir}/${*}" --dir "firefox" --stow "${STOW_PACKAGE}"

$(firefox_out_dirs):
	@mkdir -p "${@}"
