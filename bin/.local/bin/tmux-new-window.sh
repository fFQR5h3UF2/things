#!/usr/bin/env bash
set -Eeuxo pipefail

if ! which fzf >/dev/null 2>&1; then
    exit
fi

dir=$(
    {
        echo "${PWD}"
        find ~/repos/ -type d -name .git -exec dirname '{}' ';'
    } | fzf
)
cd "${dir}" || true
tmux rename-window "$(basename "${dir}")"
tmux send-keys "cd ${dir}" Enter
tmux send-keys "clear" Enter
tmux send-keys "which nvim && nvim" Enter
tmux split-window -h -c '#{pane_current_path}'
tmux split-window -v -c '#{pane_current_path}'
