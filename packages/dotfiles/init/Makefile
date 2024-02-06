INIT_DIR = ${PACKAGE_DIR}/dotfiles/init
INIT_VENV_DIR = ${HOME}/.venv
INIT_VENV_CMD = . "${INIT_VENV_DIR}/bin/activate"

.PHONY: init
init: ${OUT_TRACKER_DIR}/init/init ## Prepare environment
${OUT_TRACKER_DIR}/init/init: ${OUT_TRACKER_DIR}/init/ansible-galaxy \
							  ${OUT_TRACKER_DIR}/init/stow \
							  ${OUT_TRACKER_DIR}/init/poetry

.PHONY: init/clean
init/clean: init/clean-poetry-venv init/clean-venv ## Remove poetry venv and root venv

.PHONY: init/poetry-bin
init/poetry-bin: ${OUT_TRACKER_DIR}/init/poetry-bin ## Install poetry via pix
${OUT_TRACKER_DIR}/init/poetry-bin: ${OUT_TRACKER_DIR}/init/venv-pipx
	pipx install poetry
	@touch "${@}"

.PHONY: init/poetry-env
init/poetry-env: ${OUT_TRACKER_DIR}/init/poetry-env ## Setup poetry venv
${OUT_TRACKER_DIR}/init/poetry-env: ${OUT_TRACKER_DIR}/init/poetry-bin
	poetry -C "${DOTFILES_DIR}" env use python3
	@touch "${@}"

.PHONY: init/poetry
init/poetry: ${OUT_TRACKER_DIR}/init/poetry ## Install dependencies using poetry
${OUT_TRACKER_DIR}/init/poetry: ${OUT_TRACKER_DIR}/init/poetry-env
	poetry -C "${DOTFILES_DIR}" install --no-root
	@touch "${@}"

.PHONY: init/stow
init/stow: ${OUT_TRACKER_DIR}/init/stow ## Install stow
${OUT_TRACKER_DIR}/init/stow: ${OUT_TRACKER_DIR}/init/ansible-galaxy
	$(call ansible-install stow,stow)
	@touch "${@}"

.PHONY: init/ansible-galaxy
init/ansible-galaxy: ${OUT_TRACKER_DIR}/init/ansible-galaxy ## Install ansible collections
${OUT_TRACKER_DIR}/init/ansible-galaxy: ${OUT_TRACKER_DIR}/init/poetry
	poetry -C "${DOTFILES_DIR}" run ansible-galaxy install -r "${DOTFILES_DIR}/galaxy_requirements.yml"
	@touch "${@}"

.PHONY: init/venv
init/venv: ${OUT_TRACKER_DIR}/init/venv ## Create root venv
${OUT_TRACKER_DIR}/init/venv:
	python3 -m venv "${INIT_VENV_DIR}"
	@touch "${@}"

.PHONY: init/venv-pip
init/venv-pip: ${OUT_TRACKER_DIR}/init/venv-pip ## Upgrade pip in root venv
${OUT_TRACKER_DIR}/init/venv-pip: ${OUT_TRACKER_DIR}/init/venv
	$(INIT_VENV_CMD) && python3 -m pip install --upgrade pip
	@touch "${@}"

.PHONY: init/venv-pipx
init/venv-pipx: ${OUT_TRACKER_DIR}/init/venv-pipx ## Install pipx in root venv
${OUT_TRACKER_DIR}/init/venv-pipx: ${OUT_TRACKER_DIR}/init/venv-pip
	$(INIT_VENV_CMD) && python3 -m pip install pipx
	$(INIT_VENV_CMD) && python3 -m pipx ensurepath
	@touch "${@}"

.PHONY: init/clean-poetry-venv
init/clean-poetry-venv: ## Clean poetry venv
	-poetry -C "${DOTFILES_DIR}" env remove --all 2>/dev/null

.PHONY: init/clean-venv
init/clean-venv: ## Clean root venv
	-rm -rf "${INIT_VENV_DIR}"
