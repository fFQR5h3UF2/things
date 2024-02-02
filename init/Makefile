init_venv_dir = ${HOME}/.venv
init_venv_cmd = . "${init_venv_dir}/bin/activate"

.PHONY: init
init: ${OUT_TRACKER_DIR}/init/init
${OUT_TRACKER_DIR}/init/init: ${OUT_TRACKER_DIR}/init/ansible-galaxy \
							  ${OUT_TRACKER_DIR}/init/stow \
							  ${OUT_TRACKER_DIR}/init/poetry-no-root

.PHONY: init/clean
init/clean: init/clean-poetry-venv init/clean-venv

.PHONY: init/poetry-bin
init/poetry-bin: ${OUT_TRACKER_DIR}/init/poetry-bin
${OUT_TRACKER_DIR}/init/poetry-bin: ${OUT_TRACKER_DIR}/init/venv-pipx
	pipx install poetry
	@touch "${@}"

.PHONY: init/poetry-env
init/poetry-env: ${OUT_TRACKER_DIR}/init/poetry-env
${OUT_TRACKER_DIR}/init/poetry-env: ${OUT_TRACKER_DIR}/init/poetry-bin
	poetry env use python3
	@touch "${@}"

.PHONY: init/poetry
init/poetry: ${OUT_TRACKER_DIR}/init/poetry
${OUT_TRACKER_DIR}/init/poetry: ${OUT_TRACKER_DIR}/init/poetry-env
	poetry install
	@touch "${@}"

.PHONY: init/poetry-no-root
init/poetry-no-root: ${OUT_TRACKER_DIR}/init/poetry-no-root
${OUT_TRACKER_DIR}/init/poetry-no-root: ${OUT_TRACKER_DIR}/init/poetry-env
	poetry install --no-root
	@touch "${@}"

.PHONY: init/stow
init/stow: ${OUT_TRACKER_DIR}/init/stow
${OUT_TRACKER_DIR}/init/stow: ${OUT_TRACKER_DIR}/init/ansible-galaxy
	$(call ansible-install stow,stow)
	@touch "${@}"

.PHONY: init/ansible-galaxy
init/ansible-galaxy: ${OUT_TRACKER_DIR}/init/ansible-galaxy
${OUT_TRACKER_DIR}/init/ansible-galaxy: ${OUT_TRACKER_DIR}/init/poetry-no-root
	poetry run ansible-galaxy install -r "${PROJECT_DIR}/galaxy_requirements.yml"
	@touch "${@}"

.PHONY: init/venv
init/venv: ${OUT_TRACKER_DIR}/init/venv
${OUT_TRACKER_DIR}/init/venv:
	python3 -m venv "${init_venv_dir}"
	@touch "${@}"

.PHONY: init/venv-pip
init/venv-pip: ${OUT_TRACKER_DIR}/init/venv-pip
${OUT_TRACKER_DIR}/init/venv-pip: ${OUT_TRACKER_DIR}/init/venv
	$(init_venv_cmd) && python3 -m pip install --upgrade pip
	@touch "${@}"

.PHONY: init/venv-pipx
init/venv-pipx: ${OUT_TRACKER_DIR}/init/venv-pipx
${OUT_TRACKER_DIR}/init/venv-pipx: ${OUT_TRACKER_DIR}/init/venv-pip
	$(init_venv_cmd) && python3 -m pip install pipx
	$(init_venv_cmd) && python3 -m pipx ensurepath
	@touch "${@}"

.PHONY: init/clean-poetry-venv
init/clean-poetry-venv:
	-poetry env remove --all 2>/dev/null

.PHONY: init/clean-venv
init/clean-venv:
	-rm -rf "${init_venv_dir}"
