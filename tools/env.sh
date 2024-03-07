#!/usr/bin/env sh

# fix for https://github.com/bazelbuild/rules_go/wiki/Editor-setup
GOPACKAGESDRIVER="$(git rev-parse --show-toplevel)/tools/gopackagesdriver"
export GOPACKAGESDRIVER
