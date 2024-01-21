PACKAGES = setup shell bin nvim git firefox tmux vscode
PACKAGES_TEST = $(addprefix test-, $(PACKAGES))
PACKAGES_CLEAN = $(addprefix clean-, $(PACKAGES))
PACKAGE_MAKE = $(MAKE) -C "${@}"

.PHONY: min all test clean
.PHONY: $(PACKAGES) $(PACKAGES_TEST) $(PACKAGES_CLEAN)

min: shell bin nvim tmux
all: $(PACKAGES)
test: $(PACKAGES_TEST)
clean: $(PACKAGES_CLEAN)

bin: shell
nvim:
firefox:
tmux: shell
vscode:

$(PACKAGES):
	$(PACKAGE_MAKE) install
$(PACKAGES_TEST):
	$(PACKAGE_MAKE) test
$(PACKAGES_CLEAN):
	$(PACKAGE_MAKE) clean
