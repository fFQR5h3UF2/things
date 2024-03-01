#!/usr/bin/env sh

# fix for https://github.com/bazelbuild/rules_go/wiki/Editor-setup
GOPACKAGESDRIVER="$(dirname "${0}")/gopackagesdriver"
export GOPACKAGESDRIVER
