PACKAGES = setup shell bin nvim git udev firefox tmux vscode
PACKAGES_TEST = $(addprefix test-, $(PACKAGES))
PACKAGES_CLEAN = $(addprefix clean-, $(PACKAGES))
PACKAGES_BUILD = $(addprefix build-, $(PACKAGES))

.PHONY: min all test clean build
.PHONY: $(PACKAGES) $(PACKAGES_TEST) $(PACKAGES_BUILD) $(PACKAGES_CLEAN)

min: shell bin nvim tmux
all: $(PACKAGES)
test: $(PACKAGES_TEST)
clean: $(PACKAGES_CLEAN)
build: $(PACKAGES_BUILD)

$(PACKAGES):
	$(MAKE) --directory "${@}" install

$(PACKAGES_BUILD):
	$(MAKE) --directory "${@:build-%=%}" build

$(PACKAGES_TEST):
	$(MAKE) --directory "${@:test-%=%}" test

$(PACKAGES_CLEAN):
	$(MAKE) --directory "${@:clean-%=%}" clean
