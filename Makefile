shell::
	$(MAKE) -C shell

bin::
	$(MAKE) -C bin

nvim::
	$(MAKE) -C nvim

firefox::
	$(MAKE) -C firefox

tmux::
	$(MAKE) -C tmux

nvim_sync::
	nvim --headless "+Lazy! sync" +qa

setup::
	./scripts/setup.sh

test_makefile::
	./scripts/test_makefile.sh
