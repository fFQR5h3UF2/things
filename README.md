# [dotfiles](https://github.com/shishifubing/dotfiles)

[![License](https://img.shields.io/github/license/shishifubing/dotfiles.svg)](https://github.com/shishifubing/dotfiles/blob/main/LICENSE)
[![Version](https://img.shields.io/github/v/release/shishifubing/dotfiles?label=version)](https://github.com/shishifubing/dotfiles/releases/latest)
[![Release](https://img.shields.io/github/actions/workflow/status/shishifubing/dotfiles/release.yml?branch=main&label=release&logo=github)](https://github.com/shishifubing/dotfiles/actions/workflows/release.yml)

Things for personal use

## Usage

### Requirements

git, make, python3, python3-venv

### Help

```
Usage: make [options] [target] ...
Targets:
  repos                                Run repos/apply
  repos/apply                          Apply
  repos/clean-tf                       Clean state
  repos/docs                           Update terraform docs
  repos/import                         Run import script
  repos/init                           Terraform init
  repos/list                           Terraform state list
  bin                                  Run bin/install
  bin/install                          Install pipx packages, npm, and stow package
  bin/build                            Build stow package
  bin/test                             Test stow package
  bin/clean                            Clean stow package, clean pipx packages, clean npm
  bin/install-pipx                     Install pipx packages
  bin/install-npm                      Install npm
  bin/install-nvm                      Install nvm in ${NVM_DIR}
  bin/clean-npm                        Clean npm install tracker
  bin/clean-nvm                        Clean ${NVM_DIR} and nvm install tracker
  bin/clean-pipx                       Clean pipx packages
  vscode                               Run vscode/install
  vscode/install                       Install stow package
  vscode/build                         Build stow package
  vscode/clean                         Clean stow package
  vscode/test                          Test stow package
  ssh                                  Run ssh/personal
  ssh/personal                         Harden ssh with ssh_server_enabled = false
  ssh/server                           Harden ssh with ssh_server_enabled = true
  shell                                Run shell/install
  shell/install                        Install stow package
  shell/build                          Build stow package
  shell/clean                          Clean stow package
  shell/test                           Test stow package
  shell/remove-bashrc                  Disable current .bashrc if it is a file
  init                                 Prepare environment
  init/clean                           Remove poetry venv and root venv
  init/poetry-bin                      Install poetry via pix
  init/poetry-env                      Setup poetry venv
  init/poetry                          Install dependencies using poetry
  init/stow                            Install stow
  init/ansible-galaxy                  Install ansible collections
  init/venv                            Create root venv
  init/venv-pip                        Upgrade pip in root venv
  init/venv-pipx                       Install pipx in root venv
  init/clean-poetry-venv               Clean poetry venv
  init/clean-venv                      Clean root venv
  udev                                 Run udev/install
  udev/install                         Install stow package and reload udev rules
  gpg                                  Run gpg/instal
  gpg/install                          Install stow package
  gpg/build                            Build stow package
  gpg/test                             Test stow package
  gpg/clean                            Clean stow package
  dotfiles/tmux                        Run dotfiles/tmux/install
  dotfiles/tmux/install                Install dotfiles/tmux, install stow package
  dotfiles/tmux/build                  Build stow package
  dotfiles/tmux/test                   Test stow package
  dotfiles/tmux/clean                  Clean stow package
  dotfiles/tmux/install-dotfiles/tmux  Install dotfiles/tmux
  os                                   Run os/personal
  os/personal                          Run os hardening with os_desktop_enable = true
  os/server                            Run os hardening
  dotfiles/nvim                        Run dotfiles/nvim/install
  dotfiles/nvim/install                Install stow package
  dotfiles/nvim/build                  Build stow package
  dotfiles/nvim/test                   Test stow package
  dotfiles/nvim/clean                  Clean stow package
  dotfiles/nvim/sync                   Update Lazy packages
  firefox                              Run firefox/install
  firefox/install                      Install stow package
  firefox/setup                        Prepare directories
  firefox/build                        Build stow package
  firefox/test                         Test stow package
  firefox/clean                        Clean stow package
  git                                  Run git/install
  git/install                          Install stow package
  git/build                            Build stow package
  git/clean                            Clean stow package
  git/test                             Test stow package
  leetcode                             Run leetcode/parse
  leetcode/download                    Download last 20 submissions to ./leetcode/submissions.json
  leetcode/generate                    Generate files in ./leetcode/submissions/ from ./leetcode/submissions.json
  leetcode/update                      Download new submissions, create MR for them, merge the MR
  leetcode/format                      Run leetcode/format-black and leetcode/format-gofmt
  leetcode/format-black                Format submissions using black
  leetcode/format-gofmt                Format submissions using gofmt
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
