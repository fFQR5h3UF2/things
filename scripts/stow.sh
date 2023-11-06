#!/usr/bin/env bash
set -Eeuxo pipefail

function _stow() {
    stow  --override='.*' --dir="${PWD}" --target="${2:-${HOME}}" "${1}"
}

case "${1}" in
    git) _stow git;;
    home) _stow home;;
    nvim) _stow nvim;;
    firefox)
        for profile in "${HOME}/.mozilla/firefox/"*".default-release-"*; do
            _stow firefox "${profile}"
	done;;
    vscode)
        for dir in "Code - OSS" "Code" "VSCodium"; do
          _stow vscode "${HOME}/.config/${dir}"
	done;;
    *) echo "invalid option: ${1}"; exit 1;;
esac
