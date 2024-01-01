#!/usr/bin/env bash

IS_INTERACTIVE=
if [[ ${-} == *i* ]]; then
    IS_INTERACTIVE="1"
fi

export DOTFILES="${HOME}/repos/shishifubing/dotfiles"
. "${DOTFILES}/scripts/functions.sh"

export FZF_DEFAULT_COMMAND="fd --type f"
export FZF_COMPLETION_TRIGGER="**"

export force_color_prompt=yes
export GPG_TTY="${TTY:-}"
export EDITOR="nvim"
# user-specific configuration files
export XDG_CONFIG_HOME="${HOME}/.config"
## the main prompt variable
# https://stackoverflow.com/a/28938235
export PS1='\[\e[35;1m\]\u\[\e[m\]@\[\e[35;1m\]\h\[\e[m\] \[\e[36;1m\]\w\[\e[m\] \[\e[1m\]$(__git_ps1 "%s")\[\e[m\]\n\$ '
export PROMPT_COMMAND='_dotfiles_prompt_command'
# git prompt variables
export GIT_PS1_SHOWDIRTYSTATE=true
export GIT_PS1_SHOWUPSTREAM=auto
export GIT_PS1_STATESEPARATOR=" "
export GIT_PS1_SHOWCOLORHINTS=true
export GIT_PS1_SHOWCONFLICTSTATE=yes
export GIT_PS1_SHOWUNTRACKEDFILES=true

## all locales are overwritten
export LC_ALL="en_US.UTF-8"
export LANG="en_US.UTF-8"
## silences npm funding messages
export OPEN_SOURCE_CONTRIBUTOR="true"
# git editor
export GIT_EDITOR="nvim"

# history file location
export HISTFILE=~/.bash_history
# ignore commands starting with whitespace
export HISTCONTROL="ignorespace"
# bash history size (file size)
export HISTFILESIZE=
# bash history size (number of lines)
export HISTSIZE=10000

# android sdk
export ANDROID_HOME="${HOME}/Android/Sdk"
### path edits
export GOPATH="${HOME}/.go"
export JAVA_HOME="/usr/java/latest"

_dotfiles_add_to_path_back \
    ~/.local/share/gem/ruby/*/bin \
    ~/.local/bin \
    /usr/bin \
    "${GOPATH}/bin" \
    ~/yandex-cloud/bin \
    "${ANDROID_HOME}/tools" \
    /usr/java/latest/bin \
    /usr/mvn/latest/bin

# https://www.gnu.org/software/bash/manual/html_node/The-Shopt-Builtin.html
# vim mode for the terminal
set -o vi
# emacs mode for the terminal
#set -o emacs
# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize
# minor errors in the spelling of a directory in a cd command will be corrected
#shopt -s cdspell
# attempt spelling correction on directory names during word completion
shopt -s dirspell
# include filenames beginning with a ‘.’ in the results of filename expansion
shopt -s dotglob
# send SIGHUP to all jobs when an interactive login shell exits
shopt -s huponexit
# match filenames in a case-insensitive fashion when performing filename expansion.
shopt -s nocaseglob
# flushes the command to the history file immediately
# otherwise, this would happen only when the shell exits
shopt -s histappend
# attempt to save all lines of a multiple-line
# command in the same history entry.
shopt -s cmdhist

if [[ ${IS_INTERACTIVE} && ${TERM_PROGRAM} != "tmux" ]]; then
    if tmux has-session &>/dev/null; then
        tmux attach-session
    else
        tmux
    fi
fi

_dotfiles_source_scripts \
    /etc/profile.d/bash_completion.sh \
    /usr/share/git-core/contrib/completion/git-prompt.sh \
    /usr/share/bash-completion/completions/git \
    /usr/share/fzf/shell/key-bindings.bash \
    ~/.venv/bin/activate
