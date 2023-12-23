#!/usr/bin/env bash
set -Eeuxo pipefail

make setup_repo setup_packages home git firefox vscode nvim update_readme
. "${HOME}/.bashrc"
__source_scripts ssdfsdf "${HOME}/.bashrc"
