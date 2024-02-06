#!/usr/bin/env bash
set -uxo pipefail

owner="${1:-shishifubing}"
bot="${2:-${owner}-bot}"

function import() {
    terraform import "${@}"
}

team_id=$(gh api "/orgs/${owner}/teams/admins" --jq .id)

import "github_membership.bot" "${owner}:${bot}"
import "github_team.admins" "${team_id}"
import "github_team_membership.bot" "${team_id}:${bot}"

mapfile -t repos < <(
    gh repo list "${owner}" \
        --json "name" \
        --template '{{ range . }}{{ .name }}{{ "\n" }}{{ end }}'
)

for repo in "${repos[@]}"; do
    mapfile -t tag_protections < <(
        gh api "/repos/${owner}/${repo}/tags/protection" --jq .[].id
    )
    for tag_protection in "${tag_protections[@]}"; do
        import \
            "github_repository_tag_protection.protections[\"${repo}\"]" \
            "${repo}/${tag_protection}"
    done
    import \
        "module.branch_protections_main[\"${repo}\"].github_branch_protection.protection" \
        "${repo}:main"
    import \
        "module.branch_protections_wildcard[\"${repo}\"].github_branch_protection.protection" \
        "${repo}:*"
    import "github_branch_default.default[\"${repo}\"]" "${repo}"
    import "github_team_repository.admins[\"${repo}\"]" "${team_id}:${repo}"
done

for repo in "${repos[@]}"; do
    # gitlab's repository names cannot start with a special character
    repo_name="${repo}"
    if [[ "${repo:0:1}" == "." ]]; then
        repo_name="dot-${repo:1}"
    fi
    import "gitlab_project.repositories[\"${repo}\"]" "${owner}/${repo_name}"
done
