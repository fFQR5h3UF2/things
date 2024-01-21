#!/usr/bin/env sh
set -o errexit -o nounset -o xtrace

set +x
dry_run=
while [ "${#}" -gt 0 ]; do
    case "${1}" in
    --private_key)
        printf "%s" "${2}" >_key
        shift 2
        ;;
    --passphrase)
        printf "%s" "${2}" >_passphrase
        shift 2
        ;;
    --dry_run)
        dry_run="${2}"
        shift 2
        ;;
    esac
done
set -x

# parse the key
key=$(gpg --with-colons --batch --show-keys --with-fingerprint --keyid-format=long _key)
user=$(echo "${key}" | awk -F ":" '/uid/ { print $10 }')
key_id=$(echo "${key}" | awk -F ":" '/sec/ { print $5 }')
#fingerprint=$(awk -F ":" '/fpr/ { print $10; exit }' <<<"${key}")
#keygrip=$(awk -F ":" '/fpr/ { keygrip = $10 } END { print keygrip }' <<<"${key}")
name="${user%%<*}"
name=$(echo "${name}" | cut -c "-${#name}")
email="${user##*<}"
email=$(echo "${email}" | cut -c "-${#email}")

# setup gpg
gpg="$(dirname "${0}")/gpg.sh"
echo "
default-cache-ttl 21600
max-cache-ttl 31536000
allow-preset-passphrase
allow-loopback-pinentry
" >>~/.gnupg/gpg-agent.conf
gpg-connect-agent reloadagent /bye
"${gpg}" --import _key

# setup git
export GIT_AUTHOR_NAME="${name}"
export GIT_AUTHOR_EMAIL="${email}"
export GIT_COMMITTER_NAME="${name}"
export GIT_COMMITTER_EMAIL="${email}"
git config --global --add safe.directory "${PWD}"
git status
git config user.signingkey "${key_id}"
git config gpg.program "${gpg}"
git config commit.gpgsign true
git config tag.gpgsign true

# bump the version
cz bump --yes --changelog --version-scheme semver || {
    code="${?}"
    if [ "${code}" -eq 21 ]; then
        echo "NonIncrementExit detected, exiting"
        exit
    else
        exit "${code}"
    fi
}

# verify the new tag
new_tag="v$(cz version -p)"
git tag -v "${new_tag}"

# push the tag and the commit
if [ -z "${dry_run}" ]; then
    git push origin HEAD
    git push origin "${new_tag}"
fi
