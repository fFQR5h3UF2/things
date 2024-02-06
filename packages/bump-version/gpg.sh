#!/usr/bin/env sh
set -o errexit -o nounset -o xtrace

gpg --batch \
    -vv \
    --yes \
    --no-tty \
    --passphrase-file _passphrase \
    --pinentry-mode loopback \
    "${@}"
