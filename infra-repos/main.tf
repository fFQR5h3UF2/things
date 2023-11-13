terraform {
  backend "s3" {}

  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5"
    }
    gitlab = {
      source  = "gitlabhq/gitlab"
      version = "~> 15"
    }
    time = {
      source  = "hashicorp/time"
      version = "~> 0.9"
    }
  }
}

locals {
  owner           = "shishifubing"
  owner_url       = "https://github.com/${local.owner}"
  repo_names      = toset(data.github_repositories.repos.names)
  repo_full_names = toset(data.github_repositories.repos.full_names)
}

provider "github" {
  owner = local.owner
}

provider "gitlab" {}


data "github_repositories" "repos" {
  query           = "org:${local.owner}"
  include_repo_id = true
}

resource "github_membership" "bot" {
  username = "shishifubing-bot"
  role     = "member"
}

resource "github_team" "admins" {
  name                      = "admins"
  description               = "Grants admin rights to all shishifubing repositories"
  privacy                   = "closed"
  create_default_maintainer = true
}

resource "github_team_membership" "bot" {
  team_id  = github_team.admins.id
  username = github_membership.bot.username
  role     = "maintainer"
}

resource "github_team_repository" "admins" {
  for_each = local.repo_names

  team_id    = github_team.admins.id
  repository = each.value
  permission = "admin"
}

module "branch_protections_main" {
  for_each = local.repo_names
  source   = "./modules/branch_protection"

  config = {
    repository_id                   = each.value
    pattern                         = "main"
    enforce_admins                  = true
    required_approving_review_count = 0
    required_status_checks = {
      "commits" = {
        # https://github.com/marketplace/commitcheck
        # https://www.commitcheck.com
        contexts = ["CommitCheck"]
        strict   = true
      }
    }
  }
}

module "branch_protections_wildcard" {
  for_each   = local.repo_names
  source     = "./modules/branch_protection"
  depends_on = [module.branch_protections_main]

  config = {
    repository_id           = each.value
    pattern                 = "*"
    required_linear_history = true
    allows_deletions        = true
    allows_force_pushes     = true
    required_status_checks = {
      "commits" = {
        # https://github.com/marketplace/commitcheck
        # https://www.commitcheck.com
        contexts = ["CommitCheck"]
        strict   = true
      }
    }
  }
}

resource "github_repository_tag_protection" "protections" {
  for_each   = local.repo_names
  repository = each.value
  pattern    = "v*"
}

resource "github_branch_default" "default" {
  for_each = local.repo_names

  repository = each.value
  branch     = "main"
}

resource "github_actions_organization_permissions" "main" {
  allowed_actions      = "all"
  enabled_repositories = "all"
}

#
# gitlab stuff
#
data "gitlab_group" "group" {
  full_path = local.owner
}


resource "time_rotating" "day" {
  rotation_days = 1
}

# I have to use time_static because of https://github.com/hashicorp/terraform-provider-time/issues/118
resource "time_static" "day" {
  rfc3339 = time_rotating.day.rfc3339
}

resource "gitlab_project" "repositories" {
  for_each = local.repo_names

  lifecycle {
    # ignore all changes to not clutter logs
    ignore_changes = all
    # replace every day
    replace_triggered_by = [time_static.day]
  }

  # gitlab repository names cannot start with a special character
  name = substr(each.value, 0, 1) == "." ? format(
    "dot-%s",
    substr(each.value, 1, length(each.value))
  ) : each.value
  description = join(" ", [
    "mirror of https://github.com/${local.owner}/${each.value}",
    "[${time_static.day.rfc3339}]"
  ])
  import_url       = "https://github.com/${local.owner}/${each.value}"
  namespace_id     = data.gitlab_group.group.group_id
  visibility_level = "public"
}

/*
resource "github_repository_ruleset" "branches_main" {
  name        = "main"
  target      = "branch"
  enforcement = "active"


  conditions {
    ref_name {
      include = ["~DEFAULT_BRANCH"]
      exclude = []
    }
  }

  rules {
    creation                = true
    update                  = true
    deletion                = true
    required_linear_history = true
    required_signatures     = true
  
    pull_request {
      
    }

    branch_name_pattern {
      name     = "example"
      negate   = false
      operator = "starts_with"
      pattern  = "ex"
    }
  }
}

resource "github_repository_ruleset" "branches_other" {
  name        = "other"
  target      = "branch"
  enforcement = "active"

  conditions {
    ref_name {
      include = ["~ALL"]
      exclude = []
    }
  }

  rules {
    creation                = true
    update                  = true
    deletion                = true
    required_linear_history = true
    required_signatures     = true

    branch_name_pattern {
      name     = "example"
      negate   = false
      operator = "starts_with"
      pattern  = "ex"
    }
  }
}

resource "github_organization_ruleset" "tags" {
  name        = "tags"
  target      = "tag"
  enforcement = "active"

  conditions {
    ref_name {
      include = ["~ALL"]
      exclude = []
    }
  }

  rules {
    creation                = true
    update                  = true
    deletion                = true
    required_linear_history = true
    required_signatures     = true

    branch_name_pattern {
      name     = "example"
      negate   = false
      operator = "starts_with"
      pattern  = "ex"
    }
  }
}
*/