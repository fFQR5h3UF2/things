#!/usr/bin/env sh
set -o errexit -o nounset -o xtrace

dotfiles_dir="${HOME}/repos/shishifubing/dotfiles"
dotfiles_url="https://github.com/shishifubing/dotfiles.git"

if [ "${PWD}" != "${DOTFILES:-}" ]; then
    if [ ! -d "${dotfiles_dir}" ]; then
        mkdir -p "$(basename "${dotfiles_dir}")"
        git clone "${dotfiles_url}" "${dotfiles_dir}"
    fi
    cd "${dotfiles_dir}"
fi

make init
