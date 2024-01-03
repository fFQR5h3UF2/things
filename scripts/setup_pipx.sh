#!/usr/bin/env bash
set -Eeuxo pipefail

mapfile -t packages_pipx <packages-pipx.txt
for package in "${packages_pipx[@]}"; do
    pipx install "${package}"
done
