# bump_version

Action and scripts to bump the project version using commitizen

## Usage

```yaml
name: On main
on:
  push:
    branches:
      - main
jobs:
  bump_version:
    runs-on: ubuntu-latest
    if: "!startsWith(github.event.head_commit.message , 'bump')"
    steps:
      - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
        with:
          fetch-depth: 0
          token: ${{ secrets.CI_GITHUB_TOKEN }}
      - uses: shishifubing/dotfiles/bump_version@main
        with:
          private_key: ${{ secrets.CI_GPG_PRIVATE_KEY }}
          passphrase: ${{ secrets.CI_GPG_PASSPHRASE }}
          dry_run: 1
```
