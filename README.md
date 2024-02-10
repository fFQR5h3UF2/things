# [dotfiles](https://github.com/shishifubing/dotfiles)

[![License](https://img.shields.io/github/license/shishifubing/dotfiles.svg?style=for-the-badge)](https://github.com/shishifubing/dotfiles/blob/main/LICENSE)
[![Version](https://img.shields.io/github/v/release/shishifubing/dotfiles?label=version&style=for-the-badge)](https://github.com/shishifubing/dotfiles/releases/latest)
[![Release](https://img.shields.io/github/actions/workflow/status/shishifubing/dotfiles/release.yml?branch=main&label=release&logo=github&style=for-the-badge)](https://github.com/shishifubing/dotfiles/actions/workflows/release.yml)

Things for personal use

## Usage

### Requirements

git, make, python3, python3-venv

### Help

```
Usage: make [options] [target] ...
Targets:
  repos                            Run repos/apply
  repos/apply                      Apply
  repos/clean-tf                   Clean state
  repos/docs                       Update terraform docs
  repos/import                     Run import script
  repos/init                       Terraform init
  repos/list                       Terraform state list
  dotfiles                         Run dotfiles/install
  dotfiles/install                 Run dotfiles/install-stow-package
  dotfiles/build                   Run dotfiles/build-stow-packages
  dotfiles/setup                   Run dotfiles/init
  dotfiles/clean                   Run dotfiles/clean-stow-package
  dotfiles/install-stow-package    Install stow package
  dotfiles/uninstall-stow-package  Uninstall stow package
  dotfiles/clean-stow-package      Uninstall stow package and clean it
  dotfiles/build-stow-package      Build stow package
  dotfiles/vscode                  Run dotfiles/vscode/install
  dotfiles/vscode/install          Install stow package
  dotfiles/vscode/build            Build stow package
  dotfiles/vscode/clean            Clean stow package
  dotfiles/vscode/test             Test stow package
  dotfiles/ssh                     Run ssh/personal
  dotfiles/ssh/personal            Harden ssh with ssh_server_enabled = false
  dotfiles/ssh/server              Harden ssh with ssh_server_enabled = true
  dotfiles/init                    Prepare environment
  dotfiles/init/clean              Remove poetry venv and root venv
  dotfiles/init/poetry-bin         Install poetry via pix
  dotfiles/init/poetry-env         Setup poetry venv
  dotfiles/init/poetry             Install dependencies using poetry
  dotfiles/init/stow               Install stow
  dotfiles/init/ansible-galaxy     Install ansible collections
  dotfiles/init/venv               Create root venv
  dotfiles/init/venv-pip           Upgrade pip in root venv
  dotfiles/init/venv-pipx          Install pipx in root venv
  dotfiles/init/clean-poetry-venv  Clean poetry venv
  dotfiles/init/clean-venv         Clean root venv
  dotfiles/udev                    Run dotfiles/udev/install
  dotfiles/udev/install            Install stow package and reload udev rules
  dotfiles/os                      Run os/personal
  dotfiles/os/personal             Run os hardening with os_desktop_enable = true
  dotfiles/os/server               Run os hardening
  dotfiles/nvim/sync               Update Lazy packages
  leetcode                         Run leetcode/parse
  leetcode/download                Download last 20 submissions to ./leetcode/submissions.json
  leetcode/generate                Generate files in ./leetcode/submissions/ from ./leetcode/submissions.json
  leetcode/update                  Download new submissions, create MR for them, merge the MR
  leetcode/format                  Run leetcode/format-black and leetcode/format-gofmt
  leetcode/format-black            Format submissions using black
  leetcode/format-gofmt            Format submissions using gofmt
```

### Clone

```bash
git clone https://github.com/shishifubing/dotfiles.git ~/repos/shishifubing/dotfiles
cd ~/repos/shishifubing/dotfiles
make
```

### Init script

```bash
url="https://raw.githubusercontent.com/shishifubing/dotfiles/main/init/scripts/init"
curl -sSL "${url}" | bash
```
