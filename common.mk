OUT_DIR = out
TRACKER_DIR = ${OUT_DIR}/tracker
STOW_PACKAGE = stow
STOW_OUT_DIR = ${OUT_DIR}/${STOW_PACKAGE}
STOW_INSTALL_TARGET = ${HOME}
STOW_FILES = $(shell find "${STOW_PACKAGE}" "${STOW_OUT_DIR}" 2>/dev/null)
STOW_CMD = stow --no-folding --verbose
STOW_BUILD = $(STOW_CMD) --target "${STOW_OUT_DIR}"
STOW_INSTALL = $(STOW_CMD) --target "${STOW_INSTALL_TARGET}" --dir "${OUT_DIR}"
OUT_DIRS = ${OUT_DIR} ${TRACKER_DIR} ${STOW_OUT_DIR}

define tracker
	${TRACKER_DIR}/${1}
endef

.PHONY: install install-stow
.PHONY: clean clean-out clean-stow
.PHONY: build build-stow
.PHONY: test test-stow
.PHONY: update

install: build
setup: | $(OUT_DIRS)
build: setup
test: build
update:
clean: clean-out

${TRACKER_DIR}/%:
	touch "${@}"

$(OUT_DIR):
	mkdir -p "${@}"

${OUT_DIR}/%:
	mkdir -p "${@}"

build-stow: $(call tracker,build-stow)
$(call tracker,build-stow): $(call tracker,setup) $(STOW_FILES)
	$(STOW_BUILD) --stow "${STOW_PACKAGE}"
	touch "${@}"

install-stow: build
	$(STOW_INSTALL) --stow "${STOW_PACKAGE}"

test-stow: build
	$(STOW_INSTALL) --simulate "${STOW_PACKAGE}"

clean-stow:
	$(STOW_INSTALL) --delete "${STOW_PACKAGE}"

clean-out: clean-stow
	rm -r ./out
