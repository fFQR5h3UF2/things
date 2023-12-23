<div align="center" markdown="1">

# [`ci`][url-repo]

[![License][badge-license]][url-license]
[![Version][badge-version]][url-version]
[![Release][badge-release]][url-release]

CI stuff

</div>

## About the project

This repository contains [action](./action.yml) that launches
several [scripts](./scripts) depending on the name of the job

## Usage

### Example

Runs [bump_version](./scripts/bump_version) script

```yaml
name: On main

on:
  branches: main

jobs:
  bump_version:
    runs-on: ubuntu-latest
    container:
      image: ubuntu@sha256:1395dff3ecc43bbc9c1fb2af3b9d8c0df89ef9ef5f11f7ac69c6e0875862ef08 # 24.04
    steps:
      - run: apt-get update && apt-get install git -y && git --version
      - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
        with:
          fetch-depth: 0
          token: ${{ secrets.CI_GITHUB_TOKEN }}
      - uses: ./.
        env:
          CI_GPG_PRIVATE_KEY: ${{ secrets.CI_GPG_PRIVATE_KEY }}
          CI_GPG_PASSPHRASE: ${{ secrets.CI_GPG_PASSPHRASE }}

```

<!-- relative links -->


<!-- project links -->

[url-license]: https://github.com/shishifubing/ci/blob/main/LICENSE
[url-repo]: https://github.com/shishifubing/ci
[url-release]: https://github.com/shishifubing/ci/actions/workflows/release.yml
[url-version]: https://github.com/shishifubing/ci/releases/latest

<!-- external links -->

[url-owner]: https://github.com/shishifubing
[url-conventionalcommits]: https://conventionalcommits.org
[url-gitversion-action]: https://github.com/GitTools/actions
[url-gitversion]: https://github.com/GitTools/GitVersion
[url-actionlint]: https://github.com/rhysd/actionlint
[url-issuelabeler]: https://github.com/github/issue-labeler
[url-prlabeler]: https://github.com/actions/labeler
[url-prsizelabeler]: https://github.com/CodelyTV/pr-size-labeler

<!-- project badge links -->

[badge-license]: https://img.shields.io/github/license/shishifubing/ci.svg
[badge-release]: https://img.shields.io/github/actions/workflow/status/shishifubing/ci/release.yml?branch=main&label=release&logo=github
[badge-version]: https://img.shields.io/github/v/release/shishifubing/ci?label=version
