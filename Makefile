.POSIX:

PACKAGES = $(shell ./make/scripts/get_packages)
PACKAGES_CHANGED = $(shell ./make/scripts/get_packages changed)

OUT_DIR = ./out
OUT_PACKAGE_DIR = ${OUT_DIR}/package
OUT_TRACKER_DIR = ${OUT_DIR}/tracker
STOW_PACKAGE = stow
OUT_STOW_DIR = ${OUT_DIR}/${STOW_PACKAGE}
OUT_DIRS = $(PACKAGES:%=$(OUT_DIR)/%) $(PACKAGES:%=${OUT_TRACKER_DIR}/%) \
		   $(PACKAGES:%=${OUT_STOW_DIR}/%)
PROJECT_DIR = $(shell git rev-parse --show-toplevel)
STOW_INSTALL_DIR = ${HOME}
STOW_CMD = stow --no-folding --verbose

install_targets = $(PACKAGES:%=%/install)
.PHONY: install $(install_targets)
install: $(install_targets)
$(install_targets): %/install: %/build

build_targets = $(PACKAGES:%=%/build)
.PHONY: build $(build_targets)
build: $(build_targets)
$(build_targets): %/build: %/setup

setup_targets = $(PACKAGES:%=%/setup)
.PHONY: setup $(setup_targets)
setup: $(setup_targets)
$(setup_targets): init
init: | $(OUT_DIRS)

test_targets = $(PACKAGES:%=%/test)
.PHONY: test $(test_targets)
test: $(test_targets)
$(test_targets): %/test: %/build

clean_targets = $(PACKAGES:%=%/clean)
.PHONY: clean clean-out $(clean_targets) $(clean_tracker_targets)
clean: clean-out
clean-out: $(clean_targets)
	-rm -rf "${OUT_DIR}"
$(clean_targets): %/clean:
$(PACKAGES:%=%/clean-out):
	-rm -rf "${OUT_PACKAGE_DIR}/${*}"

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

build_stow_targets = $(PACKAGES:%=%/build-stow)
.PHONY: $(build_stow_targets)
$(build_stow_targets): %/build-stow: %/setup
	$(STOW_CMD) --target "${OUT_STOW_DIR}/${*}" --dir "${*}" --stow "${STOW_PACKAGE}"

install_stow_targets = $(PACKAGES:%=%/install-stow)
.PHONY: $(install_stow_targets)
$(install_stow_targets): %/install-stow: %/build %/build-stow
	$(STOW_CMD) --target "${STOW_INSTALL_DIR}" --dir "${OUT_STOW_DIR}" --stow "${*}"

test_stow_targets = $(PACKAGES:%=%/test-stow)
.PHONY: $(test_stow_targets)
$(test_stow_targets): %/test-stow: %/build %/build-stow
	$(STOW_CMD) --target "${STOW_INSTALL_DIR}" --dir "${OUT_STOW_DIR}" --simulate "${*}"

clean_stow_targets = $(PACKAGES:%=%/clean-stow)
.PHONY: $(clean_stow_targets)
$(clean_stow_targets): %/clean-stow:
	-$(STOW_CMD) --target "${STOW_INSTALL_DIR}" --dir "${OUT_STOW_DIR}" --delete "${*}"
	-rm -rf "${OUT_STOW_DIR}/${*}"

.PHONY: air
air:
	go run github.com/cosmtrek/air@latest

$(OUT_DIRS):
	@mkdir -p "${@}"

${TRACKER_DIR}/%:
	@mkdir -p "${@D}"
	@touch "${@}"


$(foreach package, $(PACKAGES), $(eval include ${package}/Makefile))
