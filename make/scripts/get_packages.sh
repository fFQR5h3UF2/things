#!/usr/bin/env sh
set -o errexit -o nounset #-o xtrace

changed="${1:-}"
dir="$(git rev-parse --show-toplevel)"
cd "${dir}"
find . -maxdepth 1 -type d |
    while read -r path; do
        if [ "${path}" = "." ] || [ ! -f "${path}/Makefile" ]; then
            continue
        fi
        if [ -n "${changed}" ] && [ -z "$(git diff --name-only "${path}")" ]; then
            continue
        fi
        echo "${path##*/}"
    done
