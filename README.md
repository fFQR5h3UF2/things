# [dotfiles][url-repo]

[![License][badge-license]][url-license]
[![Version][badge-version]][url-version]
[![Release][badge-workflow-release]][url-workflow-release]

Things for personal use

## About The Project

### Contents

- [ansible](./ansible/): ansible roles and playbooks
- [configs](./configs/): configuration files
- [diagrams](./diagrams/): diagrams
- [scripts](./scripts/): scripts
- [actions](./actions/): github actions
  - [bump_version](./actions/bump_version/): bump version and update changelog using commitizen
  - [kaniko](./actions/kaniko/): wrapper for kaniko
- [stow](./stow/): stow packages
  - [firefox](./stow/firefox/): firefox configuration files
  - [bin](./stow/bin/): scripts that need to be on PATH
  - [git](./stow/git/): .gitconfig
  - [home](./stow/home/): home directory configs
  - [nvim](./stow/nvim/): neovim configuration files
  - [vscode](./stow/vscode/): vscode configs

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

[url-repo]: https://github.com/shishifubing/dotfiles
[url-license]: https://github.com/shishifubing/dotfiles/blob/main/LICENSE
[url-workflow-release]: https://github.com/shishifubing/dotfiles/actions/workflows/release.yml
[url-version]: https://github.com/shishifubing/dotfiles/releases/latest
[badge-license]: https://img.shields.io/github/license/shishifubing/dotfiles.svg
[badge-workflow-release]: https://img.shields.io/github/actions/workflow/status/shishifubing/dotfiles/release.yml?branch=main&label=release&logo=github
[badge-version]: https://img.shields.io/github/v/release/shishifubing/dotfiles?label=version
