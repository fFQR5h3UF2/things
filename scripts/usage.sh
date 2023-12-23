#!/usr/bin/env bash
set -Eeuxo pipefail

curl -sSL "https://raw.githubusercontent.com/shishifubing/dotfiles/main/scripts/setup_repo" | bash
cd "${HOME}/repos/shishifubing/dotfiles"
make setup_packages home git firefox
