firefox_dir = .mozilla/firefox
firefox_profiles = $(notdir $(wildcard ${HOME}/${firefox_dir}/*.default-release-*))
firefox_targets = $(addprefix firefox/build-, $(firefox_profiles))

firefox/install: firefox/install-stow
firefox/build: firefox/build-stow
firefox/test: firefox/test-stow
firefox/clean: firefox/clean-stow

firefox/build-stow: $(firefox_targets) ;

.PHONY: $(firefox_targets)
$(firefox_targets): firefox/build-%: ${OUT_DIR}/firefox/${STOW_PACKAGE}/${firefox_dir}/%
	$(STOW_CMD) --target "${<}" --dir "firefox" --stow "${STOW_PACKAGE}"
