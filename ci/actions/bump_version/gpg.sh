#!/usr/bin/env bash
set -Eeuxo pipefail
gpg \
    --batch \
    -vv \
    --yes \
    --no-tty \
    --passphrase-file _passphrase \
    --pinentry-mode loopback \
    "${@}"
