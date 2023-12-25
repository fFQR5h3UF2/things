#!/usr/bin/env bash
set -Eeuxo pipefail

make setup home git firefox vscode nvim update_readme
. scripts/bashrc.sh
__source_scripts ssdfsdf "${HOME}/.bashrc"
