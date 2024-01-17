PACKAGES = setup shell bin nvim firefox tmux vscode

.PHONY: $(PACKAGES)

min: bin nvim tmux

bin: shell

nvim: shell

tmux: shell

$(PACKAGES):
	$(MAKE) -C $@ install

test_makefile::
	./scripts/test_makefile.sh
