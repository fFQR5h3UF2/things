INIT_VENV_DIR = ${HOME}/.venv
INIT_VENV_CMD = . "$(INIT_VENV_DIR)/bin/activate"

setup: init
clean: init-clean

.PHONY: init
init: init-ansible-galaxy

.PHONY: init-clean
init-clean: init-clean-poetry-venv init-clean-venv

.PHONY: init-poetry-bin
init-poetry-bin: init-venv-pipx
	pipx install poetry

.PHONY: init-poetry-env
init-poetry-env: init-poetry-bin
	poetry env use python3

.PHONY: init-poetry
init-poetry: init-poetry-env
	poetry install

.PHONY: init-poetry-no-root
init-poetry-no-root:
	poetry install --no-root

.PHONY: init-stow
init-stow: init-ansible-galaxy
	$(call ansible-install stow,stow)

.PHONY: init-ansible-galaxy
init-ansible-galaxy: init-poetry-no-root
	poetry run ansible-galaxy install -r "${PROJECT_DIR}/galaxy_requirements.yml"

.PHONY: init-venv
init-venv:
	python3 -m venv "${INIT_VENV_DIR}"

.PHONY: init-venv-pip
init-venv-pip: init-venv
	$(INIT_VENV_CMD) && python3 -m pip install --upgrade pip

.PHONY: init-venv-pipx
init-venv-pipx: init-venv-pip
	$(INIT_VENV_CMD) && python3 -m pip install pipx
	$(INIT_VENV_CMD) && python3 -m pipx ensurepath

.PHONY: init-clean-poetry-venv
clean-poetry-venv:
	-poetry env remove --all 2>/dev/null

.PHONY: init-clean-venv
init-clean-venv:
	-rm -rf "${INIT_VENV_DIR}"
