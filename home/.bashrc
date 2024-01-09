#!/usr/bin/env bash

# If not running interactively, don't do anything
if [[ "${-}" != *i* ]]; then
    return
fi

. "${DOTFILES:-${HOME}/repos/shishifubing/dotfiles}/scripts/bashrc.sh"
_dotfiles_tmux_start

export NVM_DIR="$HOME/.config/nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"                   # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion" # This loads nvm bash_completion
