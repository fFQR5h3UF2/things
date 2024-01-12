#!/usr/bin/env bash

# If not running interactively, don't do anything
if [[ "${-}" != *i* ]]; then
    return
fi
. "${DOTFILES:-${HOME}/repos/shishifubing/dotfiles}/scripts/bashrc.sh"
dotfiles_tmux_start
