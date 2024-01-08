#!/usr/bin/env sh
set -o errexit -o nounset -o xtrace

package="${1:?missing package}"

_stow() {
    _target="${1:-"${HOME}"}"
    mkdir -p "${_target}"
    stow --restow --override='.*' --dir="${PWD}" --target="${_target}" "${package}"
}

case "${package}" in
"firefox")
    find ~/.mozilla/firefox/ -name "*.default-release-*" |
        while read -r profile; do
            _stow "${profile}"
        done
    ;;
"vscode")
    for dir_name in "Code - OSS" "Code" "VSCodium"; do
        _stow "${HOME}/.config/${dir_name}"
    done
    ;;
"home")
    if [ ! -L ~/.bashrc ]; then
        rm -f ~/.bashrc
    fi
    _stow
    ;;
"bin" | "git" | "nvim")
    _stow
    ;;
*)
    echo "invalid package: ${package}"
    exit 1
    ;;
esac
