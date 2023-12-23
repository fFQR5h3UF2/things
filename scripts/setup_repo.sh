#!/usr/bin/env bash
set -Eeuxo pipefail

dotfiles_dir="${DOTFILES:-"${HOME}/repos/shishifubing"}"
dotfiles_url="https://github.com/shishifubing/dotfiles.git"

mkdir -p "${dotfiles_dir}"

if [[ -d "${dotfiles_dir}/.git" ]]; then
    git --git-dir "${dotfiles_dir}/.git" checkout main
    git --git-dir "${dotfiles_dir}/.git" pull
else
    git clone "${dotfiles_url}" "${dotfiles_dir}"
fi
