#!/usr/bin/env bash
set -Eeuxo pipefail

_install_os() {
    command="apt-get"
    if ! which "${command}"; then
        command="yum"
    fi
    if [[ "$(whoami)" == "root" ]]; then
        "${command}" update
        "${command}" install -y "${@}"
    else
        sudo "${command}" update
        sudo "${command}" install -y "${@}"
    fi
}

_install_pipx() {
    for package in "${@}"; do
        pipx install "${package}"
    done
}

dotfiles_dir=~/repos/shishifubing/dotfiles
dotfiles_url=https://github.com/shishifubing/dotfiles.git
mapfile -t packages_os <packages-os.txt
mapfile -t packages_pipx <packages-pipx.txt

mkdir -p "${dotfiles_dir}" ~/.local/bin ~/.ssh ~/.gnupg
chmod 0700 ~/.ssh ~/.gnupg

if ! which git; then
    _install_os git
fi
if [[ ! -d "${dotfiles_dir}" ]]; then
    git clone "${dotfiles_url}" "${dotfiles_dir}"
fi
cd "${dotfiles_dir}"

_install_os "${packages_os[@]}"
_install_pipx "${packages_pipx[@]}"

hashicorp_url="https://hashicorp-releases.yandexcloud.net"
github_url="https://github.com"
gitversion_url="${github_url}/GitTools/GitVersion/releases/download"
helm_url="https://get.helm.sh"
yc_url="https://storage.yandexcloud.net/yandexcloud-yc"
terraform_docs_url="${github_url}/terraform-docs/terraform-docs/releases/download"
k8s_url="https://dl.k8s.io/release"
glab_url="https://gitlab.com/gitlab-org/cli/-/releases"
protoc_url="https://github.com/protocolbuffers/protobuf/releases/download"

terraform_version="1.3.7"
packer_version="1.8.5"
gitversion_version="5.11.1"
kubectl_version=$(curl -Ls "${k8s_url}/stable.txt")
helm_version="v3.10.3"
yc_version=$(curl -Ls "${yc_url}/release/stable")
terraform_docs_version="v0.16.0"
glab_version="1.24.1"
protoc_version="3.15.8"

terraform_docs_distrib="terraform-docs-${terraform_docs_version}-linux-amd64.tar.gz"
terraform_distrib="terraform_${terraform_version}_linux_amd64.zip"
packer_distrib="packer_${packer_version}_linux_amd64.zip"
gitversion_distrib="gitversion-linux-x64-${gitversion_version}.tar.gz"
helm_distrib="helm-${helm_version}-linux-amd64.tar.gz"
glab_distrib="glab_${glab_version}_Linux_x86_64.tar.gz"
protoc_distrib="protoc-${protoc_version}-linux-x86_64.zip"

urls=(
    "${hashicorp_url}/terraform/${terraform_version}/${terraform_distrib}"
    "${hashicorp_url}/packer/${packer_version}/${packer_distrib}"
    "${gitversion_url}/${gitversion_version}/${gitversion_distrib}"
    "${k8s_url}/${kubectl_version}/bin/linux/amd64/kubectl"
    "${yc_url}/release/${yc_version}/linux/amd64/yc"
    "${terraform_docs_url}/${terraform_docs_version}/${terraform_docs_distrib}"
    "${helm_url}/${helm_distrib}"
    "${glab_url}/v${glab_version}/downloads/${glab_distrib}"
    "${protoc_url}/v${protoc_version}/${protoc_distrib}"
)
binaries=(
    "terraform" "packer" "gitversion" "kubectl" "yc" "helm" "terraform-docs"
    "glab" "protoc"
)

temp=$(mktemp -d)
exit_code=0
(
    cd "${temp}"
    echo "downloading"
    for url in "${urls[@]}"; do
        wget --no-verbose "${url}"
    done

    echo "unzipping"
    for zip in *.zip; do
        unzip "${zip}"
    done
    for tar in *.tar.gz; do
        tar -xvzf "${tar}"
    done
    mv ./*/helm ./bin/* ./

    echo "installing binaries"
    chmod +x "${binaries[@]}"
    mv "${binaries[@]}" ~/.local/bin/
) || {
    exit_code="${?}"
}
rm -rf "${temp}"
exit "${exit_code}"
