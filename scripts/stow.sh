#!/usr/bin/env bash
set -Eeuxo pipefail

target="${1:?missing target}"

function _stow {
    stow  --override='.*' --dir="${PWD}" --target="${2:-"${HOME}"}" "${1}"
}

if [[ "${target}" == "firefox" ]]; then
    for profile in "${HOME}/.mozilla/firefox/"*".default-release-"*; do
        _stow firefox "${profile}"
    done
elif [[ "${target}" == "vscode" ]]; then
    for dir_name in "Code - OSS" "Code" "VSCodium"; do
        dir="${HOME}/.config/${dir_name}"
	mkdir -p "${dir}"
	_stow vscode "${dir}"
    done
elif [[ -f "./${target}" ]]; then
    _stow "${target}"
else
    echo "invalid target: ${target}"
    exit 1
fi
