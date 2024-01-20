OUT_DIR = ./out
STOW_PACKAGE = stow
STOW_OUT_DIR = ${OUT_DIR}/${STOW_PACKAGE}
STOW_INSTALL_TARGET = ${HOME}
STOW_CMD = stow --no-folding --verbose
STOW_BUILD = $(STOW_CMD) --target "${STOW_OUT_DIR}"
STOW_INSTALL = $(STOW_CMD) --target "${STOW_INSTALL_TARGET}" --dir "${OUT_DIR}"
OUT_DIRS = ${OUT_DIR} ${STOW_OUT_DIR}

.PHONY: install install-stow
.PHONY: clean clean-out clean-stow
.PHONY: build build-stow
.PHONY: test test-stow
.PHONY: update

install: build
setup: | $(OUT_DIRS)
build: setup
test: build
update: install
clean: clean-out

build-stow: setup
	$(STOW_BUILD) --stow "${STOW_PACKAGE}"
install-stow: build
	$(STOW_INSTALL) --stow "${STOW_PACKAGE}"
test-stow: build
	$(STOW_INSTALL) --simulate "${STOW_PACKAGE}"
clean-stow:
	$(STOW_INSTALL) --delete "${STOW_PACKAGE}"
clean-out: clean-stow
	rm -r ./out
$(OUT_DIRS):
	mkdir -p "${@}"
