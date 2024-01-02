#!/usr/bin/env bash
set -Eeuxo pipefail
git config --global user.email "sdfsadf"
git config --global user.name "asdfsdfs"
git commit --allow-empty -m "feat: empty commit to force bump"
