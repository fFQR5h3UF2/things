include ../common.mk

MOZILLA_DIR = .mozilla/firefox
PROFILES = $(notdir $(wildcard ${HOME}/${MOZILLA_DIR}/*.default-release-*))
PROFILES_OUT_DIRS = $(addprefix ${STOW_OUT_DIR}/${MOZILLA_DIR}/, $(PROFILES))

install: install-stow
build: $(PROFILES_OUT_DIRS)
test: test-stow

$(PROFILES_OUT_DIRS): $(STOW_FILES)
	mkdir -p "${@}"
	$(STOW_CMD) --stow --target "${@}" "${STOW_PACKAGE}"
	touch "${@}"
