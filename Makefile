PACKAGES = $(shell ./make/scripts/get_packages.sh)
PACKAGES_CHANGED = $(shell ./make/scripts/get_packages.sh changed)

OUT_DIR = ./out
OUT_DIRS = $(addprefix $(OUT_DIR)/, $(PACKAGES))
PROJECT_DIR = $(shell git rev-parse --show-toplevel)
STOW_PACKAGE = stow
STOW_INSTALL_DIR = ${HOME}
STOW_CMD = stow --no-folding --verbose

install_targets = $(addsuffix /install, $(PACKAGES))
.PHONY: install $(install_targets)
install: $(install_targets)
$(install_targets): %/install: %/build

build_targets = $(addsuffix /build, $(PACKAGES))
.PHONY: build $(build_targets)
build: $(build_targets)
$(build_targets): %/build: %/setup

setup_targets = $(addsuffix /setup, $(PACKAGES))
.PHONY: setup $(setup_targets)
setup: $(setup_targets)
$(setup_targets): init/init $(OUT_DIRS)

test_targets = $(addsuffix /test, $(PACKAGES))
.PHONY: test $(test_targets)
test: $(test_targets)
$(test_targets): %/test: %/build

clean_targets = $(addsuffix /clean, $(PACKAGES))
.PHONY: clean $(clean_targets)
clean: clean-out
clean-out: $(clean_targets)
$(clean_targets): %/clean:
	-rm -rf "${OUT_DIR}/${*}"

define include_package
include ${PACKAGE}/Makefile
endef

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

build_stow_targets = $(addsuffix /build-stow, $(PACKAGES))
.PHONY: $(build_stow_targets)
$(build_stow_targets): %/build-stow: ${OUT_DIR}/%/${STOW_PACKAGE} setup
	$(STOW_CMD) --target "${<}" --dir "${*}" --stow "${STOW_PACKAGE}"

install_stow_targets = $(addsuffix /install-stow, $(PACKAGES))
.PHONY: $(install_stow_targets)
$(install_stow_targets): %/install-stow: ${OUT_DIR}/% build %/build-stow
	$(STOW_CMD) --target "${STOW_INSTALL_DIR}" --dir "${<}" --stow "${STOW_PACKAGE}"

test_stow_targets = $(addsuffix /test-stow, $(PACKAGES))
.PHONY: $(test_stow_targets)
$(test_stow_targets): %/test-stow: ${OUT_DIR}/% build %/build-stow
	$(STOW_CMD) --target "${STOW_INSTALL_DIR}" --dir "${<}" --simulate "${STOW_PACKAGE}"

clean_stow_targets = $(addsuffix /clean-stow, $(PACKAGES))
.PHONY: $(clean_stow_targets)
$(clean_stow_targets): %/clean-stow:
	-$(STOW_CMD) --target "${STOW_INSTALL_DIR}" --dir "${OUT_DIR}/${*}" --delete "${STOW_PACKAGE}"
	-rm -rf "${OUT_DIR}/${*}/stow"

.PHONY: air
air:
	go run github.com/cosmtrek/air@latest

${OUT_DIR}/%:
	@mkdir -p "${@}"

.PHONY: clean-out
clean-out:
	-rm -rf "${OUT_DIR}"

$(foreach PACKAGE, $(PACKAGES), $(eval $(include_package)))
