include make/common.mk

PACKAGES = $(shell ./make/scripts/get_packages.sh)
PACKAGES_CHANGED = $(shell ./make/scripts/get_packages.sh changed)
PACKAGES_TEST = $(addprefix test-, $(PACKAGES))
PACKAGES_TEST_CHANGED = $(addprefix test-changed-, $(PACKAGES_CHANGED))
PACKAGES_CLEAN = $(addprefix clean-, $(PACKAGES))
PACKAGES_BUILD = $(addprefix build-, $(PACKAGES))

install: $(PACKAGES)
test: $(PACKAGES_TEST)
clean: $(PACKAGES_CLEAN) clean-poetry-venv
build: $(PACKAGES_BUILD)
setup: setup-ansible-galaxy

.PHONY: air
air:
	go run github.com/cosmtrek/air@latest

.PHONY: $(PACKAGES)
$(PACKAGES): setup
	$(MAKE) --directory "${@}" install

.PHONY: $(PACKAGES_BUILD)
$(PACKAGES_BUILD): setup
	$(MAKE) --directory "${@:build-%=%}" build

.PHONY: $(PACKAGES_TEST)
$(PACKAGES_TEST): setup
	$(MAKE) --directory "${@:test-%=%}" test

.PHONY: test-changed
test-changed: $(PACKAGES_TEST_CHANGED)

.PHONY: $(PACKAGES_TEST_CHANGED)
$(PACKAGES_TEST_CHANGED):
	$(MAKE) --directory "${@:test-changed-%=%}" test

.PHONY: $(PACKAGES_CLEAN)
$(PACKAGES_CLEAN):
	$(MAKE) --directory "${@:clean-%=%}" clean
