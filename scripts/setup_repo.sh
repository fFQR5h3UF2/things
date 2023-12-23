#!/usr/bin/env bash
set -Eeuxo pipefail

dotfiles_dir="${DOTFILES:-"${HOME}/repos/shishifubing"}"
dotfiles_url="https://github.com/shishifubing/dotfiles.git"

mkdir -p "${DOTFILES}"

if [[ -d "${DOTFILES}/.git" ]]; then
    git --git-dir "${DOTFILES}/.git" checkout main
    git --git-dir "${DOTFILES}/.git" pull
else
    git clone "${dotfiles_url}" "${DOTFILES}"
fi
