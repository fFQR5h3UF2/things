#!/usr/bin/env bash
set -Eeuxo pipefail

_install_os() {
    command="apt-get"
    if ! which "${command}"; then
        command="yum"
    fi
    if [[ "$(whoami)" == "root" ]]; then
        "${command}" update
        "${command}" install -y "${@}"
    else
        sudo "${command}" update
        sudo "${command}" install -y "${@}"
    fi
}

dotfiles_dir=~/repos/shishifubing/dotfiles
dotfiles_url=https://github.com/shishifubing/dotfiles.git

mkdir -p "${dotfiles_dir}" ~/.local/bin ~/.ssh ~/.gnupg
chmod 0700 ~/.ssh ~/.gnupg

if [[ "${PWD}" != "${DOTFILES:-}" ]]; then
    if ! which git; then
        _install_os git
    fi
    if [[ ! -d "${dotfiles_dir}" ]]; then
        git clone "${dotfiles_url}" "${dotfiles_dir}"
    fi
    cd "${dotfiles_dir}"
fi

. scripts/bashrc.sh
mapfile -t packages_os <packages-os.txt
_install_os "${packages_os[@]}"
make home bin nvim setup_pipx setup_binaries #nvim_sync
