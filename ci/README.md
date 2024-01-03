# [ci][url-repo]

[![License][badge-license]][url-license]
[![Version][badge-version]][url-version]
[![Release][badge-release]][url-release]

## About the project

CI stuff:

- [Github actions](./actions/)

## Usage

### Actions

#### [bump_version](./actions/bump_version/)

Runs [bump_version](./actions/bump-version/bump_version.sh) script

```yaml
bump_version:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
      with:
        fetch-depth: 0
        token: ${{ secrets.CI_GITHUB_TOKEN }}
    - uses: shishifubing/ci/actions/bump_version@main
      with:
        private_key: ${{ secrets.CI_GPG_PRIVATE_KEY }}
        passphrase: ${{ secrets.CI_GPG_PASSPHRASE }}
```

#### [kaniko](./actions/kaniko/)

Wrapper for kaniko

```yaml
kaniko:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
    - uses: shishifubing/ci/actions/kaniko@main
      with:
        context: dir://actions/kaniko
        dockerfile: actions/kaniko/Dockerfile.test
        destination: shishifubing/test_kaniko:latest
        token: ${{ secrets.CI_DOCKERHUB_TOKEN }}
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
