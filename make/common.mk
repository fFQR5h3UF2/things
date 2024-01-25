OUT_DIR = ./out
TRACKER_DIR = ${OUT_DIR}/tracker
STOW_PACKAGE = stow
STOW_OUT_DIR = ${OUT_DIR}/${STOW_PACKAGE}
STOW_INSTALL_DIR = ${HOME}
STOW_PACKAGE_FILES = $(shell find "./${STOW_PACKAGE}" 2>/dev/null)
STOW_OUT_FILES = $(shell find "${STOW_OUT_DIR}" 2>/dev/null)
STOW_INSTALL_FILES = $(STOW_OUT_FILES:${STOW_OUT_DIR}/%=${STOW_INSTALL_DIR}/%)
STOW_CMD = stow --no-folding --verbose
STOW_INSTALL = $(STOW_CMD) --target "${STOW_INSTALL_DIR}" --dir "${OUT_DIR}"
OUT_DIRS = ${OUT_DIR} ${TRACKER_DIR} ${STOW_OUT_DIR}
ANSIBLE_CMD = poetry run ansible-playbook --ask-become-pass -i "127.0.0.1,"

define clean
	if [ -e "${1}" ]; then rm -rf "${1}"; fi
endef
define ansible-install
.PHONY: ansible-install-${1}
ansible-install-${1}:
	poetry run ansible  \
		--connection local \
		--become
		--ask-become-pass \
		"127.0.0.1," \
		-m ansible.builtin.package
		-a "name=${1} state=present"
endef

.PHONY: install
install: ${TRACKER_DIR}/install
${TRACKER_DIR}/install: ${TRACKER_DIR}/build

.PHONY: setup
setup: ${TRACKER_DIR}/setup
${TRACKER_DIR}/setup: | $(OUT_DIRS)

.PHONY: build
build: ${TRACKER_DIR}/build
${TRACKER_DIR}/build: ${TRACKER_DIR}/setup

.PHONY: test
test: ${TRACKER_DIR}/test
${TRACKER_DIR}/test: ${TRACKER_DIR}/build

.PHONY: update
update: ${TRACKER_DIR}/update

.PHONY: clean
clean: clean-out clean-venv

${TRACKER_DIR}/%:
	touch "${@}"

$(OUT_DIRS):
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
build-stow: $(STOW_OUT_FILES)
$(STOW_OUT_FILES): ${TRACKER_DIR}/build-stow
${TRACKER_DIR}/build-stow: ${TRACKER_DIR}/setup $(STOW_PACKAGE_FILES)
	$(STOW_CMD) --target "${STOW_OUT_DIR}" --stow "${STOW_PACKAGE}"
	touch "${@}"

.PHONY: install-stow
install-stow: $(STOW_INSTALL_FILES)
$(STOW_INSTALL_FILES): ${TRACKER_DIR}/install-stow
${TRACKER_DIR}/install-stow: ${TRACKER_DIR}/build
	$(STOW_INSTALL) --stow "${STOW_PACKAGE}"
	touch "${@}"

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
