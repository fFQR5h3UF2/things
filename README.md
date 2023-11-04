<div align="center" markdown="1">

# [`misc-personal-dotfiles`][url-repo]

[![License][badge-license]][url-license]
[![Version][badge-version]][url-version]
[![Release][badge-workflow-release]][url-workflow-release]

Miscellaneous things for personal use

</div>

## About The Project

### Contents

- [ansible](./ansible/) — ansible roles and playbooks (not stowed)
- [configs](./configs/) — random configuration files (not stowed)
- [diagrams](./diagrams/) - random diagrams (not stowed)
- [firefox](./firefox/) — firefox configuration files (`make firefox`)
- [git](./git/) — git configs (`make git`)
- [home](./home/) — home directory configs (`make home`)
- [nvim](./nvim/) — vim configuration files (`make nvim`)
- [scripts](./scripts/) — shell scripts (not stowed)
- [vscode](./vscode/) — vscode configs (`make vscode`)

## Usage

```bash
repo="shishifubing/misc-personal-dotfiles"
url="https://raw.githubusercontent.com/${repo}/main/scripts/setup_packages.sh"
target="${HOME}/repos/personal/misc-personal-dotfiles"

# directly execute the setup script
curl -sSL "${url}" | bash
# execute from the repo
git clone git@github.com:${repo}.git "${target}"
cd "${target}"
make setup
```

<!-- relative links -->

<!-- project links -->

[url-repo]: https://github.com/shishifubing/misc-personal-dotfiles
[url-license]: https://github.com/shishifubing/misc-personal-dotfiles/blob/main/LICENSE
[url-workflow-release]: https://github.com/shishifubing/misc-personal-dotfiles/actions/workflows/release.yml
[url-version]: https://github.com/shishifubing/misc-personal-dotfiles/releases/latest

<!-- external links -->

<!-- badge links -->

[badge-license]: https://img.shields.io/github/license/shishifubing/misc-personal-dotfiles.svg
[badge-workflow-release]: https://img.shields.io/github/actions/workflow/status/shishifubing/misc-personal-dotfiles/release.yml?branch=main&label=release&logo=github
[badge-version]: https://img.shields.io/github/v/release/shishifubing/misc-personal-dotfiles?label=version

<!-- other badge links -->
