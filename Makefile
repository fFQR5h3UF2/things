shell ::
	$(MAKE) -C shell

bin ::
	$(MAKE) -C bin

nvim_sync ::
	nvim --headless "+Lazy! sync" +qa

setup ::
	./scripts/setup.sh

test_makefile ::
	./scripts/test_makefile.sh
