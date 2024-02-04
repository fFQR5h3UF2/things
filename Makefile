# Makefile for dotfiles

PACKAGES = bin repos vscode ssh cloud/cloud/yandex shell init udev gpg tmux os make nvim firefox leetcode git
OUT_DIR = ./out
OUT_PACKAGE_DIR = ${OUT_DIR}/package
OUT_TRACKER_DIR = ${OUT_DIR}/tracker
STOW_PACKAGE = stow
OUT_STOW_DIR = ${OUT_DIR}/${STOW_PACKAGE}
OUT_DIRS = $(PACKAGES:%=$(OUT_DIR)/package/%) $(PACKAGES:%=${OUT_TRACKER_DIR}/%) \
		   $(PACKAGES:%=${OUT_STOW_DIR}/%)
STOW_INSTALL_DIR = ${HOME}
STOW_CMD = stow --no-folding --verbose
HELP_UPDATE_CMD = @printf "  %-20s %s\n" >"${*}/help.txt"

.POSIX:

.PNONY: help
help: ## Display help
	@echo "Usage: make [options] [target] ..."
	@echo "Targets:"
	@sed \
		-e '/^[a-zA-Z0-9_\/\-]*:.*##/!d' \
		-e 's/:.*##\s*/:/' \
		-e 's/^\(.\+\):\(.*\)/  $(shell tput setaf 6)\1$(shell tput sgr0):\2/' \
		$(PACKAGES:%=%/Makefile) \
		| column -c2 -t -s ":"

# generate install targets for all packages
install_targets = $(PACKAGES:%=%/install)
install_stow_targets = $(PACKAGES:%=%/install-stow)
.PHONY: install $(install_targets) $(install_stow_targets)
install: $(install_targets) ## Install packages
$(install_targets): %/install: %/build
$(install_stow_targets): %/install-stow: %/build
	$(STOW_CMD) --target "${STOW_INSTALL_DIR}" --dir "${OUT_STOW_DIR}" --stow "${*}"

# generate build targets for all packages
build_targets = $(PACKAGES:%=%/build)
build_stow_targets = $(PACKAGES:%=%/build-stow)
.PHONY: build $(build_targets) $(build_stow_targets)
build: $(build_targets) ## Build packages
$(build_targets): %/build: %/setup
$(build_stow_targets): %/build-stow: %/setup
	$(STOW_CMD) --target "${OUT_STOW_DIR}/${*}" --dir "${*}" --stow "${STOW_PACKAGE}"

# generate setup targets for all packages
setup_targets = $(PACKAGES:%=%/setup)
.PHONY: setup $(setup_targets)
setup: $(setup_targets) ## Setup packages
$(setup_targets): init
init: | $(OUT_DIRS)
$(OUT_DIRS):
	@mkdir -p "${@}"

# generate test targets for all packages
test_targets = $(PACKAGES:%=%/test)
test_stow_targets = $(PACKAGES:%=%/test-stow)
.PHONY: test $(test_targets) $(test_stow_targets)
test: $(test_targets) ## Test packages
$(test_targets): %/test: %/build
$(test_stow_targets): %/test-stow: %/build
	$(STOW_CMD) --target "${STOW_INSTALL_DIR}" --dir "${OUT_STOW_DIR}" --simulate "${*}"

# generate clean targets for all packages
clean_targets = $(PACKAGES:%=%/clean)
clean_stow_targets = $(PACKAGES:%=%/clean-stow)
.PHONY: clean clean-out $(clean_targets) $(clean_stow_targets)
clean: clean-out ## Clean packages
clean-out: $(clean_targets) ## Clean ${OUT_DIR}
	-rm -rf "${OUT_DIR}"
$(clean_targets): %/clean: %/clean-out %/clean-tracker
$(PACKAGES:%=%/clean-out): %/clean-out:
	-rm -rf "${OUT_PACKAGE_DIR}/${*}"
$(PACKAGES:%=%/clean-tracker): %/clean-tracker:
	-rm -rf "${OUT_TRACKER_DIR}/${*}"
$(clean_stow_targets): %/clean-stow:
	-$(STOW_CMD) --target "${STOW_INSTALL_DIR}" --dir "${OUT_STOW_DIR}" --delete "${*}"
	-rm -rf "${OUT_STOW_DIR}/${*}"

.PHONY: air air-start air-cmd
air: air-start ## Run air-start
air-start: ## Run air using air-cmd
	go run github.com/cosmtrek/air@latest
air-cmd: ## Run tests on changed packages
	$(MAKE) $(addsuffix /test $(shell ./make/scripts/get_packages changed))

define define ansible-install
which "${1}" || \
	poetry run ansible  \
		--connection local \
		--become \
		--ask-become-pass \
		"127.0.0.1," \
		-m ansible.builtin.package \
		-a "name=${2} state=present"
endef

# include package makefiles if help target is not specified
ifeq (,$(filter help,$(MAKECMDGOALS)))
$(foreach package,$(PACKAGES),$(eval include ${package}/Makefile))
endif
