# [dotfiles](https://github.com/shishifubing/dotfiles)

[![License](https://img.shields.io/github/license/shishifubing/dotfiles.svg)](https://github.com/shishifubing/dotfiles/blob/main/LICENSE)
[![Version](https://img.shields.io/github/v/release/shishifubing/dotfiles?label=version)](https://github.com/shishifubing/dotfiles/releases/latest)
[![Release](https://img.shields.io/github/actions/workflow/status/shishifubing/dotfiles/release.yml?branch=main&label=release&logo=github)](https://github.com/shishifubing/dotfiles/actions/workflows/release.yml)

Monorepo containing things for personal use

## About The Project

### Contents

- [actions](./actions)
- [ansible](./ansible)
- [bin](./bin)
- [cloud](./cloud)
- [configs](./configs)
- [diagrams](./diagrams)
- [firefox](./firefox)
- [git](./git)
- [home](./home)
- [images](./images)
- [nvim](./nvim)
- [repos](./repos)
- [scripts](./scripts)
- [shell](./shell)
- [tmux](./tmux)
- [vscode](./vscode)

## Usage

### Setup

```bash
curl -sSL "https://raw.githubusercontent.com/shishifubing/dotfiles/main/scripts/setup.sh" | bash
```

### Commands

- `make`, `make min`: install shell, bin nvim, tmux
- other: see [Makefile](./Makefile)
