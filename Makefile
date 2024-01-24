include make/common.mk

PACKAGES = shell os ssh gpg bin nvim git udev firefox tmux vscode
PACKAGES_TEST = $(addprefix test-, $(PACKAGES))
PACKAGES_CLEAN = $(addprefix clean-, $(PACKAGES))
PACKAGES_BUILD = $(addprefix build-, $(PACKAGES))

install: $(PACKAGES_INSTALL)
test: $(PACKAGES_TEST)
clean: $(PACKAGES_CLEAN) clean-poetry-venv
build: $(PACKAGES_BUILD)
setup: setup-ansible-galaxy

.PHONY: $(PACKAGES)
$(PACKAGES): setup
	$(MAKE) --directory "${@}" install

.PHONY: $(PACKAGES_BUILD)
$(PACKAGES_BUILD): setup
	$(MAKE) --directory "${@:build-%=%}" build

.PHONY: $(PACKAGES_TEST)
$(PACKAGES_TEST): setup
	$(MAKE) --directory "${@:test-%=%}" test

.PHONY: $(PACKAGES_CLEAN)
$(PACKAGES_CLEAN):
	$(MAKE) --directory "${@:clean-%=%}" clean
