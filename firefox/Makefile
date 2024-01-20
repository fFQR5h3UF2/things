include ../common.mk

MOZILLA_DIR = .mozilla/firefox
MOZILLA_OUT_DIR = ${STOW_OUT_DIR}/${MOZILLA_DIR}
PROFILES = $(notdir $(wildcard ${HOME}/${MOZILLA_DIR}/*.default-release-*))
PROFILES_OUT_DIRS = $(addprefix ${MOZILLA_OUT_DIR}/, $(PROFILES))

.PHONY: $(PROFILES)

install: install-stow
build: $(PROFILES)
test: test-stow
clean: clean-stow

$(PROFILES): | $(PROFILES_OUT_DIRS)
	$(STOW_CMD) --stow --target "${MOZILLA_OUT_DIR}/${@}" "${STOW_PACKAGE}"
$(PROFILES_OUT_DIRS):
	mkdir -p "${@}"
