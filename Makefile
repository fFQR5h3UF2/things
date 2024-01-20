PACKAGES = setup shell bin nvim git firefox tmux vscode
PACKAGES_TEST = $(addprefix test-, $(PACKAGES))

.PHONY: $(PACKAGES) test $(PACKAGES_TEST)

min: shell bin nvim tmux
test: $(PACKAGES_TEST)
bin: shell
nvim:
firefox:
tmux: shell
vscode:

$(PACKAGES):
	$(MAKE) -C "${@}" install
$(PACKAGES_TEST):
	$(MAKE) -C "${@}" test
