.PHONY: get-packages
get-packages: ## Search for directories containing Makefiles
	"${SCRIPT_DIR}/get_packages"

.PHONY: update-package-list
update-package-list: ## Update PACKAGES line in ${PROJECT_DIR}/Makefile
	"${SCRIPT_DIR}/get_packages" \
		| tr '\n' ' ' \
		| head -c -1 \
		| xargs -I '{}' sed -i '3c PACKAGES = {}' "${PROJECT_DIR}/Makefile"
