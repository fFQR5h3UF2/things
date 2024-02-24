<div align="center" markdown="1">

# [`plugin-sonatype-nexus-security-check`][url-repo]

[![License][badge-license]][url-license]
[![Status][badge-status-finished]][url-repo]
[![Version][badge-version]][url-version]
[![Release][badge-workflow-release]][url-workflow-release]

Security plugin for Sonatype Nexus 3

</div>

## About The Project

This plugin allows you to perform a check every time an artifact is requested from a repository

### Features

The bundle contains:

- A request handler that checks all requests to repositories
- Capability controlling the request handler
- A task that periodically updates the capability using a remote source

### BPMN diagram

![BPMN diagram]

<!-- relative links -->

[bpmn diagram]: docs/diagram.svg

<!-- project links -->

[url-repo]: https://github.com/shishifubing/plugin-sonatype-nexus-security-check
[url-license]: https://github.com/shishifubing/plugin-sonatype-nexus-security-check/blob/main/LICENSE
[url-workflow-release]: https://github.com/shishifubing/plugin-sonatype-nexus-security-check/actions/workflows/release.yml
[url-version]: https://github.com/shishifubing/plugin-sonatype-nexus-security-check/releases/latest

<!-- external links -->

<!-- badge links -->

[badge-status-finished]: https://img.shields.io/badge/status-finished-informational
[badge-license]: https://img.shields.io/github/license/shishifubing/plugin-sonatype-nexus-security-check.svg
[badge-workflow-release]: https://img.shields.io/github/actions/workflow/status/shishifubing/plugin-sonatype-nexus-security-check/release.yml?branch=main&label=release&logo=github
[badge-version]: https://img.shields.io/github/v/release/shishifubing/plugin-sonatype-nexus-security-check?label=version

<!-- other badge links -->
