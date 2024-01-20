PACKAGES = setup shell bin nvim git firefox tmux vscode

.PHONY: $(PACKAGES) test

min: bin nvim tmux
bin: shell
nvim: shell
firefox: shell
tmux: shell
vscode: shell

$(PACKAGES):
	$(MAKE) -C "${@}" install
