#!/usr/bin/env sh
set -o errexit -o nounset -o xtrace

find ~/.mozilla/firefox/ -name "*.default-release-*" |
    while read -r profile; do
        stow --restow --no-folding --target="${profile}" src
    done
