#!/usr/bin/env sh

dotfiles_cd() {
    cd "${@}" || return
    dotfiles_venv
}

dotfiles_venv() {
    _venv=
    if [ -s ./poetry.lock ]; then
        _venv=$(poetry env info -p)
    elif [ -d ./.venv ]; then
        _venv="./.venv"
    elif [ -d ./venv ]; then
        _venv="./venv"
    elif [ -d ~/venv ]; then
        _venv="${HOME}/venv"
    elif [ -d ~/.venv ]; then
        _venv="${HOME}/.venv"
    fi
    if [ -s "${_venv}/bin/activate" ]; then
        . "${_venv}/bin/activate"
    fi
}

dotfiles_docker_image_with_digest() {
    image="${1:?missing image}"
    digest=$(docker inspect --format='{{index .RepoDigests 0}}' "${image}")
    echo "${image}@${digest##*@}"
}

dotfiles_tmux_start() {
    session_name="DEFAULT"
    if [ "${TERM_PROGRAM}" = "tmux" ]; then
        return
    fi
    if ! tmux has-session -t "${session_name}"; then
        tmux new-session -d -s "${session_name}"
        tmux send-keys tmux-new-window Enter
    fi
    tmux attach-session -t "${session_name}"
}

dotfiles_prompt_command() {
    # append history lines from this session to the history file
    history -a
}

dotfiles_info_ram() {
    sudo dmidecode --type memory
}

dotfiles_source_scripts() {
    for script in "${@}"; do
        if [ -s "${script}" ]; then
            . "${script}"
        fi
    done
}

dotfiles_add_to_path_front() {
    for path in "${@}"; do
        case ":${PATH:=${path}}:" in
        *":${path}:"*) ;;
        *) PATH="${path}:${PATH}" ;;
        esac
    done
}

## create a certificate secret
dotfiles_kubernetes_secret_create_sertificate() {
    name="${1:?missing name}"
    namespace="${2:-default}"
    key="${3:-${name}.key}"
    certificate="${4:-${name}.crt}"

    kubectl create secret tls "${name}" \
        --key "${key}" \
        --cert "${certificate}" \
        --namespace "${namespace}"

}

## modify current context
dotfiles_kubernetes_context() {
    ns=$(kubectl get ns | fzf)
    kubectl config set-context --current --namespace="${ns}"
}

## create a service account and everything needed
dotfiles_kubernetes_service_account_full() {
    namespace="${1}"
    account="${2}"
    role="${3}"
    rolebinding="${4}"
    roletype="${5:-Role}"

    kubernetes_service_account "${namespace}" "${account}"
    kubernetes_rolebinding "${namespace}" "${account}" "${role}" "${rolebinding}"
}

dotfiles_kubernetes_rolebinding() {
    namespace="${1}"
    account="${2}"
    role="${3}"
    rolebinding="${4:-${role}-rolebinding}"
    roletype="${5:-Role}"
    apigroup="${6:-rbac.authorization.k8s.io}"
    if [ "${roletype}" = "ClusterRole" ]; then
        apigroup="cluster.${apigroup}"
    fi

    dotfiles_kubernetes_apply "
        apiVersion: rbac.authorization.k8s.io/v1
        kind: RoleBinding
        metadata:
          name: ${rolebinding}
          namespace: ${namespace}
        roleRef:
          apiGroup: ${apigroup}
          kind: Role
          name: ${role}
        subjects:
        - namespace: ${namespace}
          kind: ServiceAccount
          name: ${account}
    "
}

dotfiles_kubernetes_service_account() {
    namespace="${1}"
    account="${2}"
    dotfiles_kubernetes_apply "
        apiVersion: v1
        kind: ServiceAccount
        metadata:
            name: ${account}
            namespace: ${namespace}
    "
}

dotfiles_kubernetes_apply() {
    echo "${1:?missing yaml}" | kubectl apply -f -
}

# get api url
dotfiles_kubernetes_api() {
    kubectl cluster-info | grep 'Kubernetes master' | awk '/http/ { print $NF }'
}

## check open ports
dotfiles_net_ports_list() {
    sudo ss -tulpn | grep LISTEN
}

dotfiles_net_connections_list() {
    sudo netstat -nputw
}

dotfiles_net_check_dns() {
    dig "${@}" +nostats +nocomments +nocmd
}

# add windows 10 uefi entry to grub
dotfiles_setup_grub_add_windows_10_uefi() {
    # exec tail -n +4 $0
    # this line needs to be in the file, without it
    # commands will not be recognized
    source_grub
    echo "input where the EFI partition is mounted"
    read -r partition
    fs_uuid=$(sudo grub-probe --target=fs_uuid "${partition}/EFI/Microsoft/Boot/bootmgfw.efi")
    entry=$(
        cat - <<EOF
        # Windows 10 EFI entry
        if [ "\${grub_platform}" == "efi" ]; then
            menuentry "Microsoft Windows 10 UEFI" {
                insmod part_gpt
                insmod fat
                insmod search_fs_uuid
                insmod chain
                search --fs-uuid --set=root "${fs_uuid}"
                chainloader /EFI/Microsoft/Boot/bootmgfw.efi
            }
        fi
EOF
    )
    echo "${entry}"
    echo
    echo "is that okay?"
    read -r answer
    if [ "${answer}" != "n" ] && [ "${answer}" != "N" ]; then
        echo "${entry}" | sudo tee -a "/etc/grub.d/40_custom"
        source_grub
    else
        setup_grub_add_windows_10_uefi
    fi
}
