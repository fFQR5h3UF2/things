#STOW_INSTALL_TARGET = /etc/udev
#TARGET_DIR = ${STOW_OUT_DIR}/rules.d
#TARGET = ${TARGET_DIR}/99-rules.rules
#STOW_INSTALL := sudo $(STOW_INSTALL)


#udev//build: ${TARGET}
#${TARGET}: ./99-custom.rules ${TARGET_DIR}
#	envsubst <"${<}" >"${TARGET}"

#${TARGET_DIR}:
#	@mkdir -p "${@}"

#test: test-stow

udev: udev/install ## Run udev/install
udev/install: #udev/trigger-after-install udev/install-stow ## Install stow package and reload udev rules

.PHONY: uddev/trigger-after-install
udev/trigger-after-install: udev/install-stow # Reload udev rules
	sudo sh -c "udevadm control --reload-rules && udevadm trigger"
