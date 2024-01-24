OUT_DIR = ./out
TRACKER_DIR = ${OUT_DIR}/tracker
STOW_PACKAGE = stow
STOW_OUT_DIR = ${OUT_DIR}/${STOW_PACKAGE}
STOW_INSTALL_TARGET = ${HOME}
STOW_FILES = $(shell find "${STOW_PACKAGE}" "${STOW_OUT_DIR}" 2>/dev/null)
STOW_CMD = stow --no-folding --verbose
STOW_BUILD = $(STOW_CMD) --target "${STOW_OUT_DIR}"
STOW_INSTALL = $(STOW_CMD) --target "${STOW_INSTALL_TARGET}" --dir "${OUT_DIR}"
OUT_DIRS = ${OUT_DIR} ${TRACKER_DIR} ${STOW_OUT_DIR}
ANSIBLE_CMD = poetry run ansible-playbook --ask-become-pass -i "127.0.0.1,"

define clean
	if [ -e "${1}" ]; then rm -rf "${1}"; fi
endef

.PHONY: install
install: build

.PHONY: setup
setup: | $(OUT_DIRS)

.PHONY: build
build: setup

.PHONY: test
test: build

.PHONY: update
update:

.PHONY: clean
clean: clean-out clean-venv

${TRACKER_DIR}/%:
	touch "${@}"

$(OUT_DIR):
	mkdir -p "${@}"

${OUT_DIR}/%:
	mkdir -p "${@}"

.PHONY: setup-poetry-env
setup-poetry-env:
	poetry env use python3

.PHONY: setup-poetry
setup-poetry: setup-poetry-env
	poetry install

.PHONY: setup-poetry-no-root
setup-poetry-no-root: setup-poetry-env
	poetry install --no-root

.PHONY: setup-ansible-galaxy
setup-ansible-galaxy: setup-poetry-no-root
	poetry run ansible-galaxy install -r galaxy-requirements.yml

.PHONY: build-stow
build-stow: setup
	$(STOW_BUILD) --stow "${STOW_PACKAGE}"

.PHONY: install-stow
install-stow: build
	$(STOW_INSTALL) --stow "${STOW_PACKAGE}"

.PHONY: test-stow
test-stow: build
	$(STOW_INSTALL) --simulate "${STOW_PACKAGE}"

.PHONY: clean-stow
clean-stow:
	if [ -d "${STOW_OUT_DIR}" ]; then $(STOW_INSTALL) --delete "${STOW_PACKAGE}"; fi

.PHONY: clean-out
clean-out: clean-stow
	$(call clean,${OUT_DIR})

.PHONY: clean-poetry-venv
clean-poetry-venv:
	poetry env remove --all
