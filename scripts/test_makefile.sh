#!/usr/bin/env bash
set -Eeuxo pipefail

export DOTFILES="${PWD}"
make setup git firefox vscode update_readme
. scripts/bashrc.sh
_dotfiles_source_scripts ssdfsdf "${HOME}/.bashrc"
