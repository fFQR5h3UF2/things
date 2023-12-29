#!/usr/bin/env bash
set -Eeuxo pipefail

mkdir -p ~/.local/bin ~/repos ~/.ssh ~/.gnupg
chmod 0700 ~/.ssh ~/.gnupg

dotfiles_dir="${HOME}/repos/shishifubing/dotfiles"
dotfiles_url="https://github.com/shishifubing/dotfiles.git"
mkdir -p "${dotfiles_dir}"
if [[ -d "${dotfiles_dir}/.git" ]]; then
	git --git-dir "${dotfiles_dir}/.git" checkout main
	git --git-dir "${dotfiles_dir}/.git" pull
else
	git clone "${dotfiles_url}" "${dotfiles_dir}"
fi
cd "${dotfiles_dir}"

packages=(
	make git curl wget unzip stow gpg python3 python3-pip python3-venv
	gpg-agent shellcheck shfmt sudo
)
if [[ "$(whoami)" == "root" ]]; then
	apt-get update
	apt-get install -y "${packages[@]}"
else
	sudo apt-get update
	sudo apt-get install -y "${packages[@]}"
fi

python3 -m venv --symlinks --clear --upgrade-deps --prompt 'home' ~/.venv
# shellcheck source=/dev/null.
. ~/.venv/bin/activate
pip install commitizen=="3.13.0" pre-commit=="3.6.0"
cz version --project

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

echo "prepare the work directory"
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
