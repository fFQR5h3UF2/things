make_dir = ${PROJECT_DIR}/make

.PHONY: make/get-packages
make/get-packages: ## Search for directories containing Makefiles
	"${make_dir}/scripts/get_packages"

.PHONY: make/update-package-list
make/update-package-list: ## Update PACKAGES line in ./Makefile
	"${make_dir}/scripts/get_packages" \
		| tr '\n' ' ' \
		| head -c -1 \
		| xargs -I '{}' sed -i '3c PACKAGES = {}' ./Makefile
