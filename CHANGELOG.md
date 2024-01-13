# Changelog

## v0.39.0 (2024-01-13)

### Feat

- **functions**: switch to sh from bash (#82)

## v0.38.0 (2024-01-12)

### Feat

- remove _ from function names, source nvim in the proper bashrc file (#81)

## v0.37.0 (2024-01-11)

### Feat

- sign git push if asked, add hostname to tmux statusline (#80)

## v0.36.0 (2024-01-10)

### Feat

- activate venv in new tmux windows, strip trailing whitespace (#79)

## v0.35.0 (2024-01-09)

### Feat

- simplify tmux, simplify lualine, disable json schemastore (#78)

## v0.34.0 (2024-01-08)

### Feat

- **nvim**: set colorcolumn color, refactor config structure (#77)

## v0.33.0 (2024-01-08)

### Feat

- **nvim**: switch to sonokai theme (#76)

## v0.32.0 (2024-01-08)

### Feat

- move stow to root, add a script to kill tmux popup sessions (#75)
- move stow to root, kill tmux popup sessions

## v0.31.0 (2024-01-07)

### Feat

- **tmux**: pass only action type to the popup script (#74)

## v0.30.1 (2024-01-06)

### Refactor

- **stow**: rewrite from bash to sh (#73)

## v0.30.0 (2024-01-06)

### Feat

- **tmux**: improve popup handling (#72)

## v0.29.0 (2024-01-05)

### Feat

- **tmux**: autokill popups (#71)

## v0.28.0 (2024-01-05)

### Feat

- **tmux**: add floating terminal windows (#70)

## v0.27.0 (2024-01-05)

### Feat

- **nvim**: remove bufferline (#69)

## v0.26.0 (2024-01-05)

### Feat

- **tmux**: switch theme to tokyonight (#68)

## v0.25.0 (2024-01-05)

### Feat

- **nvim**: add snippets (#67)

## v0.24.0 (2024-01-04)

### Feat

- **nvim**: move all configuration inside lua/shishifubing (#66)

## v0.23.0 (2024-01-04)

### Feat

- **nvim**: disable lualine separators (#65)

## v0.22.1 (2024-01-04)

### Fix

- specify image tags alongside digests (#63)

## v0.22.0 (2024-01-04)

### Feat

- **bump_version**: use prebuilt image (#62)

## v0.21.0 (2024-01-04)

### Feat

- **images**: add commitizen image (#61)

## v0.20.1 (2024-01-03)

### Refactor

- **tmux**: rename new window script and use sh (#60)

## v0.20.0 (2024-01-03)

### Feat

- **repos**: move infra-repos to this repository (#59)

## v0.19.0 (2024-01-03)

### Feat

- **cloud**: move cloud infra to this repo (#58)

## v0.18.0 (2024-01-03)

### Feat

- **actions**: move github actions to this repo (#57)

## v0.17.0 (2024-01-03)

### Feat

- **nvim**: add ansible support (#56)

## v0.16.0 (2024-01-03)

### Feat

- remove docker image (#55)

## v0.15.1 (2024-01-03)

### Fix

- **update-readme**: invalid usage text (#54)

## v0.15.0 (2024-01-03)

### Feat

- install npm and isort (#52)

## v0.14.0 (2024-01-03)

### Feat

- **packages**: move all packages to packages dir (#51)

## v0.13.0 (2024-01-03)

### Feat

- build docker image (#50)

## v0.12.0 (2024-01-02)

### Feat

- **nvim**: add buffer keymaps, move cmp keymaps to keymaps.lua (#49)

## v0.11.1 (2024-01-02)

### Fix

- **nvim**: fix neodev setup, reformat keymaps a bit (#48)

## v0.11.0 (2024-01-02)

### Feat

- **nvim**: add bufferline (#47)

## v0.10.0 (2024-01-02)

### Feat

- **nvim**: use prettier for yaml formatting, enable autoread (#45)
- **nvim**: add listchars (#44)
- **tmux**: make main pane bigger (#42)
- **setup**: install cargo (#40)
- **tmux**: open nvim upon creating a window (#38)
- **nvim**: swith theme to rose-pine (#37)
- **nvim**: switch to conform from nullls (#32)
- **tmux**: add a shortcut and a script to improve window creation (#31)
- **tmux**: add a shortcut and a script to create windows
- **setup**: install ruff (#28)
- **nvim**: add null-ls plugin, fix plugin configs (#27)
- **nvim**: change telescope keymaps, move options to another file (#26)
- **nvim**: add ruler, add stylua hook, enable autorefactor (#25)
- **bashrc**: source fzf keybindings (#24)
- **bashrc**: if not running in tmux, either create a new session or attach (#21)
- **setup**: install pre-commit to the venv (#18)

### Fix

- **nvim**: remove custom lsp autoformatting, use only conform (#43)
- **nvim**: fix treesitter highlighting, rename plugins (#39)
- output project version
- use command instead of variable for tty

### Refactor

- **nvim**: move telescope keymaps to function (#41)
- **nvim**: move everything out of the init file (#36)
- **nvim**: split all plugins into separate files (#35)
- **nvim**: split init file further (#34)
- **nvim**: move keymaps to another file (#30)
- **nvim**: move everything to lua/, remove unused files (#29)
- **scripts**: refactor a bit (#23)
- **scripts**: refactor scripts a bit

## v0.9.2 (2023-12-23)

## v0.9.1 (2023-12-23)

### Fix

- **home**: fix invalid path

## v0.9.0 (2023-12-23)

### Feat

- move main .bashrc file to scripts

### Fix

- invalid dotfiles dir
- use nullglob before stowing firefox
- unbound variables in scripts

## v0.8.0 (2023-12-17)

### Feat

- **scripts**: add __info_ram function

## v0.7.0 (2023-12-12)

### Feat

- **home**: set HISTCONTROL to ignorespace

## v0.6.2 (2023-11-12)

### Refactor

- **vscode**: remove unused workspace config

## v0.6.1 (2023-11-08)

## v0.6.0 - 2023-11-08

<!-- Automatically generated in https://github.com/shishifubing/misc-dotfiles/actions/runs/6805127969 -->
<!-- Release notes generated using configuration in .github/release.yml at v0.6.0 -->
### What's Changed

- feat(home): clean up the prompt by @q1feq3qzi60u in https://github.com/shishifubing/misc-dotfiles/pull/7

**Full Changelog**: https://github.com/shishifubing/misc-dotfiles/compare/v0.5.0...v0.6.0

## v0.5.0 - 2023-11-07

<!-- Automatically generated in https://github.com/shishifubing/misc-dotfiles/actions/runs/6791454281 -->
<!-- Release notes generated using configuration in .github/release.yml at v0.5.0 -->
### What's Changed

- feat: remove PROMPT_COMMAND by @q1feq3qzi60u in https://github.com/shishifubing/misc-dotfiles/pull/5

**Full Changelog**: https://github.com/shishifubing/misc-dotfiles/compare/v0.2.3...v0.5.0

## v0.2.3 - 2023-11-06

<!-- Automatically generated in https://github.com/shishifubing/misc-dotfiles/actions/runs/6777685082 -->
<!-- Release notes generated using configuration in .github/release.yml at v0.2.3 -->
### New Contributors

- @shishifubing-bot made their first contribution in https://github.com/shishifubing/misc-dotfiles/pull/3

**Full Changelog**: https://github.com/shishifubing/misc-dotfiles/compare/v0.2.2...v0.2.3

## v0.2.2 - 2023-11-06

<!-- Automatically generated in https://github.com/shishifubing/misc-dotfiles/actions/runs/6771278763 -->
<!-- Release notes generated using configuration in .github/release.yml at v0.2.2 -->
### What's Changed

- feat: change dotfiles path by @q1feq3qzi60u in https://github.com/shishifubing/misc-dotfiles/pull/1
- feat: move bash out of makefile by @q1feq3qzi60u in https://github.com/shishifubing/misc-dotfiles/pull/2

### New Contributors

- @q1feq3qzi60u made their first contribution in https://github.com/shishifubing/misc-dotfiles/pull/1

**Full Changelog**: https://github.com/shishifubing/misc-dotfiles/compare/v0.2.0...v0.2.2

## v0.2.0 - 2023-03-18

<!-- Automatically generated in https://github.com/shishifubing/misc-personal-dotfiles/actions/runs/4457739322 -->
### Features

- **export**: add JAVA_HOME, add mvn to PATH by @tiandaoburen in [#28](https://github.com/shishifubing/misc-personal-dotfiles/pull/28)

**Full Changelog**: https://github.com/shishifubing/misc-personal-dotfiles/compare/v0.1.295...v0.2.0

## v0.1.296 - 2023-03-14

<!-- Automatically generated in https://github.com/shishifubing/misc-personal-dotfiles/actions/runs/4421006453 -->
**Full Changelog**: https://github.com/shishifubing/misc-personal-dotfiles/compare/v0.1.295...v0.1.296

## v0.1.295 - 2023-03-13

<!-- Automatically generated in https://github.com/shishifubing/misc-personal-dotfiles/actions/runs/4410366739 -->
### Documentation changes

- **readme**: add version and release badges by @tiandaoburen in [#25](https://github.com/shishifubing/misc-personal-dotfiles/pull/25)

**Full Changelog**: https://github.com/shishifubing/misc-personal-dotfiles/compare/v0.1.291...v0.1.295

## v0.1.291 - 2023-03-12

### Feature

- **gitconfig**: add .gitconfig management by @tiandaoburen in [#12](https://github.com/shishifubing/misc-personal-dotfiles/pull/12)
- **scripts**: remove unused scripts by @tiandaoburen in [#6](https://github.com/shishifubing/misc-personal-dotfiles/pull/6)
- **setup**: improve the script by @tiandaoburen in [#5](https://github.com/shishifubing/misc-personal-dotfiles/pull/5)
- **setup**: improve the script by @tiandaoburen in [#8](https://github.com/shishifubing/misc-personal-dotfiles/pull/8)
- **setup**: move the setup script to this repo by @tiandaoburen in [#3](https://github.com/shishifubing/misc-personal-dotfiles/pull/3)

### Bug Fix

- **gitconfig**: change email and gpg key by @tiandaoburen in [#13](https://github.com/shishifubing/misc-personal-dotfiles/pull/13)

### Documentation

- **readme**: add a comment by @tiandaoburen in [#11](https://github.com/shishifubing/misc-personal-dotfiles/pull/11)
- **readme**: add a heading by @tiandaoburen in [#15](https://github.com/shishifubing/misc-personal-dotfiles/pull/15)
- **readme**: add a license shield by @tiandaoburen in [#10](https://github.com/shishifubing/misc-personal-dotfiles/pull/10)
- **readme**: add conventional commits badge by @tiandaoburen in [#20](https://github.com/shishifubing/misc-personal-dotfiles/pull/20)
- **readme**: center the header by @tiandaoburen in [#14](https://github.com/shishifubing/misc-personal-dotfiles/pull/14)
- **readme**: change 'Features' to 'Contents' by @tiandaoburen in [#16](https://github.com/shishifubing/misc-personal-dotfiles/pull/16)
- **readme**: change headings by @tiandaoburen in [#18](https://github.com/shishifubing/misc-personal-dotfiles/pull/18)
- **readme**: fix usage section by @tiandaoburen in [#9](https://github.com/shishifubing/misc-personal-dotfiles/pull/9)
- **readme**: move links to the bottom by @tiandaoburen in [#4](https://github.com/shishifubing/misc-personal-dotfiles/pull/4)
- **readme**: remove 'About The Project' by @tiandaoburen in [#17](https://github.com/shishifubing/misc-personal-dotfiles/pull/17)
- **readme**: remove in-progress badge by @tiandaoburen in [#7](https://github.com/shishifubing/misc-personal-dotfiles/pull/7)

**Full Changelog**: https://github.com/shishifubing/misc-personal-dotfiles/compare/v0.1.0...v0.1.291
