INIT_DIR = ${PACKAGE_DIR}/dotfiles/init
INIT_OUT_DIR = ${OUT_PACKAGE_DIR}/dotfiles/init
INIT_TRACKER_DIR = ${INIT_OUT_DIR}/trackers
INIT_VENV_DIR = ${HOME}/.venv
INIT_VENV_CMD = . "${INIT_VENV_DIR}/bin/activate"

.PHONY: dotfiles/init
dotfiles/init: ${INIT_TRACKER_DIR}/init ## Prepare environment
${INIT_TRACKER_DIR}/init: ${INIT_TRACKER_DIR}/ansible-galaxy \
						  ${INIT_TRACKER_DIR}/stow \
						  ${INIT_TRACKER_DIR}/poetry

.PHONY: dotfiles/init/clean
dotfiles/init/clean: dotfiles/init/clean-poetry-venv dotfiles/init/clean-venv ## Remove poetry venv and root venv

.PHONY: dotfiles/init/poetry-bin
dotfiles/init/poetry-bin: ${INIT_TRACKER_DIR}/poetry-bin ## Install poetry via pix
${INIT_TRACKER_DIR}/poetry-bin: ${INIT_TRACKER_DIR}/venv-pipx
	pipx install poetry
	@touch "${@}"

.PHONY: dotfiles/init/poetry-env
dotfiles/init/poetry-env: ${INIT_TRACKER_DIR}/poetry-env ## Setup poetry venv
${INIT_TRACKER_DIR}/poetry-env: ${INIT_TRACKER_DIR}/poetry-bin
	poetry -C "${DOTFILES_DIR}" env use python3
	@touch "${@}"

.PHONY: dotfiles/init/poetry
dotfiles/init/poetry: ${INIT_TRACKER_DIR}/poetry ## Install dependencies using poetry
${INIT_TRACKER_DIR}/poetry: ${INIT_TRACKER_DIR}/poetry-env
	poetry -C "${DOTFILES_DIR}" install --no-root
	@touch "${@}"

.PHONY: dotfiles/init/stow
dotfiles/init/stow: ${INIT_TRACKER_DIR}/stow ## Install stow
${INIT_TRACKER_DIR}/stow: ${INIT_TRACKER_DIR}/ansible-galaxy
	$(call ansible-install stow,stow)
	@touch "${@}"

.PHONY: dotfiles/init/ansible-galaxy
dotfiles/init/ansible-galaxy: ${INIT_TRACKER_DIR}/ansible-galaxy ## Install ansible collections
${INIT_TRACKER_DIR}/ansible-galaxy: ${INIT_TRACKER_DIR}/poetry
	poetry -C "${DOTFILES_DIR}" run ansible-galaxy install -r "${DOTFILES_DIR}/galaxy_requirements.yml"
	@touch "${@}"

.PHONY: dotfiles/init/venv
dotfiles/init/venv: ${INIT_TRACKER_DIR}/venv ## Create root venv
${INIT_TRACKER_DIR}/venv:
	python3 -m venv "${INIT_VENV_DIR}"
	@touch "${@}"

.PHONY: dotfiles/init/venv-pip
dotfiles/init/venv-pip: ${INIT_TRACKER_DIR}/venv-pip ## Upgrade pip in root venv
${INIT_TRACKER_DIR}/venv-pip: ${INIT_TRACKER_DIR}/venv
	$(INIT_VENV_CMD) && python3 -m pip install --upgrade pip
	@touch "${@}"

.PHONY: dotfiles/init/venv-pipx
dotfiles/init/venv-pipx: ${INIT_TRACKER_DIR}/venv-pipx ## Install pipx in root venv
${INIT_TRACKER_DIR}/venv-pipx: ${INIT_TRACKER_DIR}/venv-pip
	$(INIT_VENV_CMD) && python3 -m pip install pipx
	$(INIT_VENV_CMD) && python3 -m pipx ensurepath
	@touch "${@}"

.PHONY: dotfiles/init/clean-poetry-venv
dotfiles/init/clean-poetry-venv: ## Clean poetry venv
	-poetry -C "${DOTFILES_DIR}" env remove --all 2>/dev/null

.PHONY: dotfiles/init/clean-venv
dotfiles/init/clean-venv: ## Clean root venv
	-rm -rf "${INIT_VENV_DIR}"
