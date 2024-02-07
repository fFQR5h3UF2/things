DOTFILES_DIR = ${PACKAGE_DIR}/dotfiles
DOTFILES_OUT_DIR = ${OUT_DIR}/dotfiles
DOTFILES_OUT_STOW_DIR = ${DOTFILES_OUT_DIR}/${DOTFILES_STOW_OUT_PACKAGE}
DOTFILES_OUT_FIREFOX_DIR = ${DOTFILES_OUT_STOW_DIR}/${DOTFILES_FIREFOX_DIR}
DOTFILES_INSTALL_DIR = ${HOME}
DOTFILES_STOW_CMD = stow --no-folding --verbose
DOTFILES_STOW_INSTALL_CMD = $(DOTFILES_STOW_CMD) --target "${DOTFILES_INSTALL_DIR}" --dir "${DOTFILES_OUT_DIR}"
DOTFILES_STOW_OUT_PACKAGE = stow
DOTFILES_STOW_PACKAGES_STATIC = shell tmux terraform bin nvim gpg git
DOTFILES_STOW_PACKAGES_STATIC_TARGETS = $(DOTFILES_STOW_PACKAGES_STATIC:%=dotfiles/build-stow-package-%)
DOTFILES_FIREFOX_DIR = .mozilla/firefox
DOTFILES_FIREFOX_PROFILES = $(notdir $(wildcard ${HOME}/${DOTFILES_FIREFOX_DIR}/*.default-release-*))
DOTFILES_FIREFOX_TARGETS = $(DOTFILES_FIREFOX_PROFILES:%=dotfiles/build-stow-package-firefox-%)
DOTFILES_FIREFOX_OUT_DIRS = $(DOTFILES_FIREFOX_PROFILES:%=${DOTFILES_OUT_FIREFOX_DIR}/%)

.PHONY: dotfiles/install
dotfiles/install: dotfiles/install-stow-package  ## Run dotfiles/install-stow-package

.PHONY: dotfiles/install-stow-package
dotfiles/install-stow-package: dotfiles/build-stow-package ## Install stow package
	$(DOTFILES_STOW_INSTALL_CMD) --stow "${DOTFILES_STOW_OUT_PACKAGE}"

.PHONY: dotfiles/uninstall-stow-package
dotfiles/uninstall-stow-package: ## Uninstall stow package
	-$(DOTFILES_STOW_INSTALL_CMD) --delete "${DOTFILES_STOW_OUT_PACKAGE}"

.PHONY: dotfiles/clean-stow-package
dotfiles/clean-stow-package: dotfiles/uninstall-stow-package ## Uninstall stow package and clean it
	-rm -rf "${DOTFILES_OUT_STOW_DIR}"

.PHONY: dotfiles/build-stow-package
dotfiles/build-stow-package: $(DOTFILES_STOW_PACKAGES_STATIC_TARGETS) dotfiles/build-stow-package-firefox ## Build stow package

.PHONY: $(DOTFILES_STOW_PACKAGES_STATIC_TARGETS)
$(DOTFILES_STOW_PACKAGES_STATIC_TARGETS): dotfiles/build-stow-package-%: ${DOTFILES_OUT_STOW_DIR}
	rsync -a "${DOTFILES_DIR}/${*}/" "${DOTFILES_OUT_STOW_DIR}/"

.PHONY: dotfiles/build-stow-package-firefox
dotfiles/build-stow-package-firefox: $(DOTFILES_FIREFOX_TARGETS)

.PHONY: $(DOTFILES_FIREFOX_TARGETS)
$(DOTFILES_FIREFOX_TARGETS): dotfiles/build-stow-package-firefox-%: $(DOTFILES_FIREFOX_OUT_DIRS)
	rsync -a "${DOTFILES_DIR}/firefox/" "${DOTFILES_OUT_FIREFOX_DIR}/${*}/"

${DOTFILES_OUT_STOW_DIR} $(DOTFILES_FIREFOX_OUT_DIRS):
	@mkdir -p "${@}"
