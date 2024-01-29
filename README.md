# [dotfiles](https://github.com/shishifubing/dotfiles)

[![License](https://img.shields.io/github/license/shishifubing/dotfiles.svg)](https://github.com/shishifubing/dotfiles/blob/main/LICENSE)
[![Version](https://img.shields.io/github/v/release/shishifubing/dotfiles?label=version)](https://github.com/shishifubing/dotfiles/releases/latest)
[![Release](https://img.shields.io/github/actions/workflow/status/shishifubing/dotfiles/release.yml?branch=main&label=release&logo=github)](https://github.com/shishifubing/dotfiles/actions/workflows/release.yml)

Things for personal use

## About The Project

### Contents

- [bin](./bin)
- [bump_version](./bump_version)
- [check-pr-changes](./check-pr-changes)
- [cloud](./cloud)
- [diagrams](./diagrams)
- [firefox](./firefox)
- [git](./git)
- [.github](./.github)
- [gpg](./gpg)
- [home](./home)
- [images](./images)
- [init](./init)
- [kaniko](./kaniko)
- [make](./make)
- [nvim](./nvim)
- [os](./os)
- [repos](./repos)
- [scripts](./scripts)
- [shell](./shell)
- [ssh](./ssh)
- [tmux](./tmux)
- [udev](./udev)
- [vscode](./vscode)

## Usage

### Setup

Requires git, make, python3, python3-venv

```bash
url="https://raw.githubusercontent.com/shishifubing/dotfiles/main/init/scripts/init.sh"
curl -sSL "${url}" | bash
```

### Commands

- `make`, `make install` - install
- other: see [Makefile](./Makefile)
