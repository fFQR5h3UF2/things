# Makefile for dotfiles

PACKAGES = ./dotfiles ./dotfiles/vscode ./dotfiles/ssh ./dotfiles/init ./dotfiles/udev ./dotfiles/os ./dotfiles/scripts repos cloud/yandex leetcode
PROJECT_DIR = $(shell git rev-parse --show-toplevel)
OUT_DIR = ${PROJECT_DIR}/out
OUT_PACKAGE_DIR = ${OUT_DIR}/packages
OUT_PACKAGE_DIRS = $(PACKAGES:%=$(OUT_PACKAGE_DIR)/%)
OUT_DIRS = $(OUT_PACKAGE_DIRS) $(OUT_PACKAGE_DIRS:%=%/trackers)
PACKAGE_DIR = ${PROJECT_DIR}/packages
SCRIPT_DIR = ${PROJECT_DIR}/scripts

.POSIX:

.PNONY: help
help: ## Display help
	@echo "Usage: make [options] [target] ..."
	@echo "Targets:"
	@sed \
		-e '/^[a-zA-Z0-9_\/\-]*:.*##/!d' \
		-e 's/:.*##\s*/:/' \
		-e 's/^\(.\+\):\(.*\)/  $(shell tput setaf 6)\1$(shell tput sgr0):\2/' \
		$(PACKAGES:%=${PACKAGE_DIR}/%/Makefile) \
		| column -c2 -t -s ":"

# generate phony targets for all packages
.PHONY: $(PACKAGES)

# generate install targets for all packages
install_targets = $(PACKAGES:%=%/install)
.PHONY: install $(install_targets)
install: $(install_targets) ## Install packages
$(install_targets): %/install: %/build

# generate build targets for all packages
build_targets = $(PACKAGES:%=%/build)
.PHONY: build $(build_targets)
build: $(build_targets) ## Build packages
$(build_targets): %/build: %/setup

# generate setup targets for all packages
setup_targets = $(PACKAGES:%=%/setup)
.PHONY: setup $(setup_targets)
setup: $(setup_targets) ## Setup packages
$(setup_targets): $(OUT_DIRS)
$(OUT_DIRS):
	@mkdir -p "${@}"

# generate test targets for all packages
test_targets = $(PACKAGES:%=%/test)
.PHONY: test $(test_targets)
test: $(test_targets) ## Test packages
$(test_targets): %/test: %/build

# generate clean targets for all packages
clean_targets = $(PACKAGES:%=%/clean)
.PHONY: clean clean-out $(clean_targets)
clean: clean-out ## Clean packages
clean-out: $(clean_targets) ## Clean ${OUT_DIR}
	-rm -rf "${OUT_DIR}"
$(clean_targets): %/clean: %/clean-out
$(PACKAGES:%=%/clean-out): %/clean-out:
	-rm -rf "${OUT_PACKAGE_DIR}/${*}"
$(PACKAGES:%=%/clean-trackers): %/clean-trackers:
	-rm -rf "${OUT_PACKAGE_DIR}/trackers/${*}"

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
$(foreach package,$(PACKAGES),$(eval -include ${PACKAGE_DIR}/${package}/Makefile))
include ${SCRIPT_DIR}/Makefile
endif
