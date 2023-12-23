#!/usr/bin/env bash
set -Eeuxo pipefail

job="${GITHUB_JOB:?missing job}"

apt-get update
apt-get install -y make git curl wget unzip stow

make "${job}"
