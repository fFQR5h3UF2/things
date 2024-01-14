#!/usr/bin/env bash

. "${DOTFILES:-"${HOME}/repos/shishifubing/dotfiles"}/shell/scripts/bashrc.sh"
if [[ "${-}" != *i* ]]; then
    return
fi
tmux-start
