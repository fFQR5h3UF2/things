#!/usr/bin/env bash
set -Eeuxo pipefail

git config --global --add safe.directory "${PWD}"
gpg="$(dirname "${0}")/gpg.sh"
python3 -m venv .venv
. .venv/bin/activate
pip install commitizen=="3.13.0"

(
    set +x
    printf "%s" "${CI_GPG_PRIVATE_KEY:?missing gpg private key}" >_key
    printf "%s" "${CI_GPG_PASSPHRASE:?missing gpg passphrase}" >_passphrase
)

key=$(gpg --with-colons --batch --show-keys --with-fingerprint --keyid-format=long _key)
user=$(awk -F ":" '/uid/ { print $10 }' <<<"${key}")
key_id=$(awk -F ":" '/sec/ { print $5 }' <<<"${key}")
#fingerprint=$(awk -F ":" '/fpr/ { print $10; exit }' <<<"${key}")
#keygrip=$(awk -F ":" '/fpr/ { keygrip = $10 } END { print keygrip }' <<<"${key}")

echo "
default-cache-ttl 21600
max-cache-ttl 31536000
allow-preset-passphrase
allow-loopback-pinentry
" >>~/.gnupg/gpg-agent.conf
gpg-connect-agent reloadagent /bye
"${gpg}" --import _key

name="${user%%<*}"
name="${name::-1}"
email="${user##*<}"
email="${email::-1}"
export GIT_AUTHOR_NAME="${name}"
export GIT_AUTHOR_EMAIL="${email}"
export GIT_COMMITTER_NAME="${name}"
export GIT_COMMITTER_EMAIL="${email}"

git status
git config user.signingkey "${key_id}"
git config gpg.program "${gpg}"
git config commit.gpgsign true
git config tag.gpgsign true

cz bump --yes --changelog --version-scheme semver || {
    code="${?}"
    if [[ "${code}" -eq 21 ]]; then
        echo "NonIncrementExit detected, exiting"
        exit
    else
        exit "${code}"
    fi
}

new_tag="v$(cz version -p)"
git tag -v "${new_tag}"
if [[ -z "${DRY_RUN:-}" ]]; then
    git push origin HEAD
    git push origin "${new_tag}"
fi
