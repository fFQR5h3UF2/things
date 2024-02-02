firefox_dir = .mozilla/firefox
firefox_stow_out_dir = ${OUT_STOW_DIR}/firefox/${firefox_dir}
firefox_profiles = $(notdir $(wildcard ${HOME}/${firefox_dir}/*.default-release-*))
firefox_targets = $(firefox_profiles:%=firefox/build-%)
firefox_out_dirs = $(firefox_profiles:%=${firefox_stow_out_dir}/%)

firefox: firefox/install
firefox/install: firefox/install-stow
firefox/setup: | $(firefox_out_dirs)
firefox/build: firefox/build-stow
firefox/test: firefox/test-stow
firefox/clean: firefox/clean-stow

firefox/build-stow: $(firefox_targets) ;

.PHONY: $(firefox_targets)
$(firefox_targets): firefox/build-%:
	$(STOW_CMD) --target "${firefox_stow_out_dir}/${*}" --dir "firefox" --stow "${STOW_PACKAGE}"

$(firefox_out_dirs):
	@mkdir -p "${@}"
