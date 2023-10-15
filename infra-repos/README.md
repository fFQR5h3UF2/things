<div align="center" markdown="1">

# [`infra-repos-shishifubing`][url-repo]

[![License][badge-license]][url-license]
[![Version][badge-version]][url-version]
[![Terraform][badge-workflow-terraform]][url-workflow-terraform]

Terraform module managing [shishifubing][url-owner] organization

</div>

## About The Project

This terraform module's main purpose is making repositories uniform

### Features

- Manages:

  - branch protection rules
  - default branches
  - github action permissions
  - tag protection rules

- Mirrors all repositories in [shishifubing][url-owner] to [Gitlab][url-owner-gitlab]

  > **Note**
  >
  > Pull mirroring is a premium Gitlab feature,
  > so all Gitlab repositories are destroyed and then imported to "_mirror_" them

## Usage

> **Note**
>
> GitHub's servers are "eventually consistent", not "immediately consistent".
> If you encounter errors (especially code 422), retry the operation
>
> Code 404 is a sign of an invalid token, check it

### CI

- Create a branch
- Commit
- PR
- Merge

### Manually

```bash
# export auth variables
. ./scripts/variables.sh
# update the infrastructure
make
```

### Regenerate module documentation

```bash
make docs
```

## Getting started

[Setup an s3 bucket, setup terraform][url-setup]

```bash
# export auth variables
. ./scripts/variables.sh
# initialize the backend
make init
# clean the state (if you need to)
make clean
# import existing repositories (if you need to)
# full import takes around 10 minutes because of the number of resources and
# Github's rate limiting
make import
# update the infrastructure
make
```

<!-- relative links -->

[branch_protection]: modules/branch_protection
[repository]: modules/repository

<!-- project links -->

[url-repo]: https://github.com/shishifubing/infra-repos-shishifubing
[url-license]: https://github.com/shishifubing/infra-repos-shishifubing/blob/main/LICENSE
[url-workflow-terraform]: https://github.com/shishifubing/infra-repos-shishifubing/actions/workflows/terraform.yml?branch=main
[url-version]: https://github.com/shishifubing/infra-repos-shishifubing/releases/latest

<!-- external links -->

[url-owner]: https://github.com/shishifubing
[url-owner-gitlab]: https://gitlab.com/shishifubing
[url-setup]: https://github.com/shishifubing/infra-cloud-shishifubing.com/tree/main/cloud/yandex#setup-terraform-backend-and-local-environment

<!-- badge links -->

[badge-workflow-terraform]: https://img.shields.io/github/actions/workflow/status/shishifubing/infra-repos-shishifubing/terraform.yml?branch=main&label=terraform&logo=github
[badge-license]: https://img.shields.io/github/license/shishifubing/infra-repos-shishifubing.svg
[badge-version]: https://img.shields.io/github/v/release/shishifubing/infra-repos-shishifubing?label=version

<!-- BEGIN_TF_DOCS -->

## Requirements

| Name                                                            | Version |
| --------------------------------------------------------------- | ------- |
| <a name="requirement_github"></a> [github](#requirement_github) | ~> 5    |
| <a name="requirement_gitlab"></a> [gitlab](#requirement_gitlab) | ~> 15   |
| <a name="requirement_time"></a> [time](#requirement_time)       | ~> 0.9  |

## Providers

| Name                                                      | Version |
| --------------------------------------------------------- | ------- |
| <a name="provider_github"></a> [github](#provider_github) | 5.39.0  |
| <a name="provider_gitlab"></a> [gitlab](#provider_gitlab) | 15.11.0 |
| <a name="provider_time"></a> [time](#provider_time)       | 0.9.1   |

## Modules

| Name                                                                                                                 | Source                      | Version |
| -------------------------------------------------------------------------------------------------------------------- | --------------------------- | ------- |
| <a name="module_branch_protections_main"></a> [branch_protections_main](#module_branch_protections_main)             | ./modules/branch_protection | n/a     |
| <a name="module_branch_protections_wildcard"></a> [branch_protections_wildcard](#module_branch_protections_wildcard) | ./modules/branch_protection | n/a     |

## Resources

| Name                                                                                                                                                               | Type        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| [github_actions_organization_permissions.main](https://registry.terraform.io/providers/integrations/github/latest/docs/resources/actions_organization_permissions) | resource    |
| [github_branch_default.default](https://registry.terraform.io/providers/integrations/github/latest/docs/resources/branch_default)                                  | resource    |
| [github_membership.bot](https://registry.terraform.io/providers/integrations/github/latest/docs/resources/membership)                                              | resource    |
| [github_repository_tag_protection.protections](https://registry.terraform.io/providers/integrations/github/latest/docs/resources/repository_tag_protection)        | resource    |
| [github_team.admins](https://registry.terraform.io/providers/integrations/github/latest/docs/resources/team)                                                       | resource    |
| [github_team_membership.bot](https://registry.terraform.io/providers/integrations/github/latest/docs/resources/team_membership)                                    | resource    |
| [github_team_repository.admins](https://registry.terraform.io/providers/integrations/github/latest/docs/resources/team_repository)                                 | resource    |
| [gitlab_project.repositories](https://registry.terraform.io/providers/gitlabhq/gitlab/latest/docs/resources/project)                                               | resource    |
| [time_rotating.day](https://registry.terraform.io/providers/hashicorp/time/latest/docs/resources/rotating)                                                         | resource    |
| [time_static.day](https://registry.terraform.io/providers/hashicorp/time/latest/docs/resources/static)                                                             | resource    |
| [github_repositories.repos](https://registry.terraform.io/providers/integrations/github/latest/docs/data-sources/repositories)                                     | data source |
| [gitlab_group.group](https://registry.terraform.io/providers/gitlabhq/gitlab/latest/docs/data-sources/group)                                                       | data source |

## Inputs

No inputs.

## Outputs

No outputs.

<!-- END_TF_DOCS -->
