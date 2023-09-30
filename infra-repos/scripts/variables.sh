#!/usr/bin/env bash

GITHUB_TOKEN=$(secret-tool lookup github "[repo, admin:org, workflow] personal"
)
GITLAB_TOKEN=$(secret-tool lookup gitlab "[api] personal")
AWS_ACCESS_KEY_ID=$(secret-tool lookup bucket-terraform-admin-personal access-key)
AWS_SECRET_ACCESS_KEY=$(secret-tool lookup bucket-terraform-admin-personal secret-key)

export AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY GITHUB_TOKEN GITLAB_TOKEN