#!/usr/bin/env bash
set -Eeuxo pipefail

which make || apt-get install -y build-essential
make setup_repo setup_packages home git firefox vscode nvim update_readme
. "${HOME}/.bashrc"
__source_scripts ssdfsdf "${HOME}/.bashrc"
