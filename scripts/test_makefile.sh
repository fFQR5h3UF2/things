#!/usr/bin/env sh
set -o errexit -o nounset -o xtrace

export DOTFILES="${PWD}"
make setup git firefox vscode update_readme
. scripts/bashrc.sh
dotfiles_source_scripts ssdfsdf "${HOME}/.bashrc"
