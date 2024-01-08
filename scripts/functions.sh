#!/usr/bin/env bash

_dotfiles_docker_image_digest() {
    docker inspect --format='{{index .RepoDigests 0}}' "${1:?missing image}"
}

_dotfiles_tmux_start() {
    local session_name="DEFAULT"
    if [[ "${TERM_PROGRAM}" == "tmux" ]]; then
        return
    fi

    if ! tmux has-session -t "${session_name}" &>/dev/null; then
        tmux new-session -d -s "${session_name}"
        tmux send-keys tmux-new-window Enter
    fi
    tmux attach-session -t "${session_name}"
}

_dotfiles_prompt_command() {
    # append history lines from this session to the history file
    history -a
}

_dotfiles_info_ram() {
    sudo dmidecode --type memory
}

_dotfiles_source_scripts() {
    for script in "${@}"; do
        if [[ -f "${script}" ]]; then
            . "${script}"
        fi
    done
}

## create a certificate
_dotfiles_crypto_certificate_create() {
    local file_name domains

    file_name="${1}"
    shift
    read -ra domains <<<"${@}"
    domains_string="DNS.1:localhost"

    for ((i = 0; i < "${#}"; i++)); do
        domains_string+=",DNS.$((i + 2)):${domains[${i}]}"
    done

    openssl req \
        -x509 \
        -newkey rsa:4096 \
        -sha256 \
        -days 3560 \
        -nodes \
        -keyout "${file_name}.key" \
        -out "${file_name}.crt" \
        -subj "/CN=${file_name}" \
        -extensions san \
        -config <(
            echo "[req]"
            echo "distinguished_name=req"
            echo "[san]"
            echo "subjectAltName=${domains_string}"
        )
}

_dotfiles_add_to_path_back() {
    for argument in "${@}"; do
        if [[ ${PATH} != *"${argument}"* ]]; then
            export PATH="${PATH}:${argument}"
        fi
    done
}

## create a certificate secret
_dotfiles_kubernetes_secret_create_sertificate() {

    local name key certificate namespace

    name="${1}"
    namespace="${2:-default}"
    key="${3:-${name}.key}"
    certificate="${4:-${name}.crt}"

    kubectl create secret tls "${name}" \
        --key "${key}" \
        --cert "${certificate}" \
        --namespace "${namespace}"

}

## modify current context
_dotfiles_kubernetes_context() {
    kubectl config set-context --current --namespace="${1}"
}

## create a service account and everything needed
_dotfiles_kubernetes_service_account_full() {
    local account namespace role rolebinding
    namespace="${1}"
    account="${2}"
    role="${3}"
    rolebinding="${4}"
    roletype="${5:-Role}"

    kubernetes_service_account "${namespace}" "${account}"
    kubernetes_rolebinding \
        "${namespace}" "${account}" "${role}" "${rolebinding}"
}

_dotfiles_kubernetes_rolebinding() {
    local account roletype apigroup namespace role rolebinding

    namespace="${1}"
    account="${2}"
    role="${3}"
    rolebinding="${4:-${role}-rolebinding}"
    roletype="${5:-Role}"
    apigroup="${6:-rbac.authorization.k8s.io}"
    if [[ ${roletype} == "ClusterRole" ]]; then
        apigroup="cluster.${apigroup}"
    fi

    _dotfiles_kubernetes_apply "
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

_dotfiles_kubernetes_service_account() {
    local account namespace
    namespace="${1}"
    account="${2}"
    _dotfiles_kubernetes_apply "
        apiVersion: v1
        kind: ServiceAccount
        metadata:
            name: ${account}
            namespace: ${namespace}
    "
}

_dotfiles_kubernetes_apply() {
    kubectl apply -f - <<<"${1:?missing yaml}"
}

# get api url
_dotfiles_kubernetes_api() {
    kubectl cluster-info | grep 'Kubernetes master' | awk '/http/ { print $NF }'
}

## check open ports
_dotfiles_net_ports_list() {
    sudo ss -tulpn | grep LISTEN
}

_dotfiles_net_connections_list() {
    sudo netstat -nputw
}

_dotfiles_net_check_dns() {
    dig "${@}" +nostats +nocomments +nocmd
}

# add windows 10 uefi entry to grub
_dotfiles_setup_grub_add_windows_10_uefi() {
    local fs_uuid
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
    if [[ ${answer} != "n" && ${answer} != "N" ]]; then
        echo "${entry}" | sudo tee -a "/etc/grub.d/40_custom"
        source_grub
    else
        setup_grub_add_windows_10_uefi
    fi
}
