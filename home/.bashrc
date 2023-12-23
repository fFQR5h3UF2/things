#!/usr/bin/env bash

# If not running interactively, don't do anything
if [[ "${-}" != *i* ]]; then
    return
fi

export DOTFILES="${DOTFILES}:-"${HOME}/repos/shishifubing/dotfiles"}"
. "${DOTFILES}/scripts/bashrc.sh"
