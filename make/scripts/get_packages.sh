#!/usr/bin/env sh
set -o errexit -o nounset #-o xtrace

changed="${1:-}"
dir="$(git rev-parse --show-toplevel)"
cd "${dir}"
find . -maxdepth 1 |
    while read -r path; do
        if [ ! -f "${path}/Makefile" ]; then
            continue
        fi
        if [ -n "${changed}" ] && [ -z "$(git diff --name-only "${path}")" ]; then
            continue
        fi
        echo "${path##*/}"
    done
