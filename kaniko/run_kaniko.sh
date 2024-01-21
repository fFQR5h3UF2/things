#!/usr/bin/env sh
set -o errexit -o nounset -o xtrace

set +x
while [ "${#}" -gt 0 ]; do
    case "${1}" in
    --context)
        CONTEXT="${2}"
        shift 2
        ;;
    --dockefile)
        DOCKERFILE="${2}"
        shift 2
        ;;
    --destination)
        DESTINATION="${2}"
        shift 2
        ;;
    --token)
        TOKEN="${2}"
        shift 2
        ;;
    --user)
        USER="${2}"
        shift 2
        ;;
    --auth_target)
        AUTH_TARGET="${2}"
        shift 2
        ;;
    --dry_run)
        DRY_RUN="${2}"
        shift 2
        ;;
    esac
done
set -x

if [ "${DRY_RUN:-}" ]; then
    /kaniko/executor \
        --context="${CONTEXT}" \
        --dockerfile="${DOCKERFILE}" \
        --reproducible \
        --no-push
    exit
fi

(
    set +x
    auth=$(printf "%s:%s" "${USER}" "${TOKEN}" | base64 -w 0)
    cat - >/kaniko/.docker/config.json <<EOF
{ "auths": { "${AUTH_TARGET}": { "auth": "${auth}" } } }
EOF
)
/kaniko/executor \
    --context="${CONTEXT}" \
    --dockerfile="${DOCKERFILE}" \
    --destination="${DESTINATION}" \
    --reproducible
