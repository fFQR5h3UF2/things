OUT_DIR = ./out
INSTALL_TRACKER = ${OUT_DIR}/install
STOW_PACKAGE = stow
STOW_OUT_DIR = ${OUT_DIR}/${STOW_PACKAGE}
STOW_INSTALL_TARGET = ${HOME}
STOW_CMD = stow --no-folding --verbose
STOW_BUILD = $(STOW_CMD) --stow --target "${STOW_OUT_DIR}" "${STOW_PACKAGE}"
STOW_INSTALL = $(STOW_CMD) --target "${STOW_INSTALL_TARGET}" --dir "${OUT_DIR}"
DIR_LAYOUT = ${OUT_DIR} ${STOW_OUT_DIR}

.PHONY: install clean build test install-stow clean-out clean-stow test-stow

install: ${INSTALL_TRACKER}

clean: clean-out

build: $(DIR_LAYOUT)

${INSTALL_TRACKER}: install-stow
	touch "${INSTALL_TRACKER}"

build-stow: ${DIR_LAYOUT}
	if [ -d "${STOW_PACKAGE}" ]; then $(STOW_BUILD) fi

install-stow: build
	$(STOW_INSTALL) --stow "${STOW_PACKAGE}"

test-stow: build
	$(STOW_INSTALL) --simulate "${STOW_PACKAGE}"

clean-stow:
	$(STOW_INSTALL) --delete "${STOW_PACKAGE}"

clean-out: clean-stow
	rm -r ./out

$(DIR_LAYOUT):
	mkdir -p "${@}"
