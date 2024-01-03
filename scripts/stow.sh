#!/usr/bin/env bash
set -Eeuxo pipefail

package="${1:?missing package}"

_stow() {
    local target="${1:-"${HOME}"}"
    mkdir -p "${target}"
    stow --override='.*' --dir="${PWD}" --target="${target}" "${package}"
}

if [[ "${package}" == "firefox" ]]; then
    shopt -s nullglob
    for profile in "${HOME}/.mozilla/firefox/"*".default-release-"*; do
        _stow "${profile}"
    done
elif [[ "${package}" == "vscode" ]]; then
    for dir_name in "Code - OSS" "Code" "VSCodium"; do
        dir="${HOME}/.config/${dir_name}"
        mkdir -p "${dir}"
        _stow "${dir}"
    done
elif [[ -d "./${package}" ]]; then
    _stow
else
    echo "missing package ${package}"
    exit 1
fi
