# [dotfiles](https://github.com/shishifubing/dotfiles)

[![License](https://img.shields.io/github/license/shishifubing/dotfiles.svg)](https://github.com/shishifubing/dotfiles/blob/main/LICENSE)
[![Version](https://img.shields.io/github/v/release/shishifubing/dotfiles?label=version)](https://github.com/shishifubing/dotfiles/releases/latest)
[![Release](https://img.shields.io/github/actions/workflow/status/shishifubing/dotfiles/release.yml?branch=main&label=release&logo=github)](https://github.com/shishifubing/dotfiles/actions/workflows/release.yml)

Things for personal use

## About The Project

### Contents

- [ansible](./ansible/): ansible roles and playbooks
  - [setup](./ansible/roles/setup/): setup role
  - [sonar](./ansible/roles/sonar/): sonar role
- [configs](./configs/): configuration files
- [diagrams](./diagrams/): diagrams
- [scripts](./scripts/): scripts
- [actions](./actions/): github actions
  - [bump_version](./actions/bump_version/): bump version and update changelog using commitizen
  - [kaniko](./actions/kaniko/): wrapper for kaniko
- [firefox](./firefox/): firefox configuration files (`make firefox`)
- [bin](./bin/): scripts that have to be on PATH (`make bin`)
  - [tmux-new-window](./bin/.local/bin/tmux-new-window):
    select a directory using fzf in the new tmux window
  - [tmux-popup](./bin/.local/bin/tmux-popup):
    toggle a tmux popup
  - [tmux-kill-popups](./bin/.local/bin/tmux-kill-popups):
    kill popups assotiated with a session
- [git](./git/): .gitconfig (`make git`)
- [home](./home/): home directory configs (`make home`)
  - [.bashrc](./home/.bashrc): .bashrc file
  - [.terraformrc.hcl](./home/.terraformrc.hcl): terraform config
  - [.tmux.conf](./home/.tmux.confi): tmux config
- [nvim](./nvim/): neovim configuration files (`make nvim`)
  - [init.lua](./nvim/.config/nvim/init.lua): just loads [lua/shishifubing](./nvim/.config/nvim/lua/shishifubing/)
  - [lazy-lock.json](./nvim/.config/nvim/lazy-lock.json): lock file for nvim packages
  - [lua/shishifubing](./nvim/.config/nvim/lua/shishifubing/): actual configuration files
    - [mapleader](./nvim/.config/nvim/lua/shishifubing/mapleader.lua): set mapleader
    - [lazy](./nvim/.config/nvim/lua/shishifubing/lazy.lua): package manager setup
    - [options](./nvim/.config/nvim/lua/shishifubing/options.lua): vim options
    - [autocmd](./nvim/.config/nvim/lua/shishifubing/autocmd.lua): autocommands
    - [filetypes](./nvim/.config/nvim/lua/shishifubing/filetypes.lua): filetypes
    - [keymaps](./nvim/.config/nvim/lua/shishifubing/keymaps.lua): keymaps
- [vscode](./vscode/): vscode configs (`make vscode`)

## Usage

### Setup

<!-- start setup usage -->

```bash
curl -sSL "https://raw.githubusercontent.com/shishifubing/dotfiles/main/scripts/setup.sh" | bash
```

<!-- end setup usage -->

### Action [bump_version](./actions/bump_version/)

Runs [bump_version](./actions/bump-version/bump_version.sh) script

```yaml
bump_version:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
      with:
        fetch-depth: 0
        token: ${{ secrets.CI_GITHUB_TOKEN }}
    - uses: shishifubing/dotfiles/actions/bump_version@main
      with:
        private_key: ${{ secrets.CI_GPG_PRIVATE_KEY }}
        passphrase: ${{ secrets.CI_GPG_PASSPHRASE }}
```

### Action [kaniko](./actions/kaniko/)

```yaml
kaniko:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
    - uses: shishifubing/dotfiles/actions/kaniko@main
      with:
        context: dir://actions/kaniko
        dockerfile: actions/kaniko/Dockerfile.test
        destination: shishifubing/test_kaniko:latest
        token: ${{ secrets.CI_DOCKERHUB_TOKEN }}
```

<!-- end usage -->
