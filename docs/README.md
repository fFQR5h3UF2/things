# docs

## laptop setup

- download and validate Proxmox Virtual Environment:
  - https://www.proxmox.com/en/downloads
- install Proxmox Virtual Environment in Gnome Boxes
  - get debian version from `support table` - https://pve.proxmox.com/pve-docs/pve-admin-guide.html#faq-support-table
  - enable nested virtualization:
    - https://pve.proxmox.com/wiki/Nested_Virtualization
  - start network service:
    - `sudo systemctl --now enable virtnetworkd.service``
  - start image - https://pve.proxmox.com/wiki/Quick_installation:
    - set hostname as `proxmox.localhost`
    - add `proxmox.localhost` to /etc/hosts
- setup main VM:
  - download and verify `Fedora Workstation` image:
    - link: https://fedoraproject.org/workstation/download
  - download and verify `Fedora CoreOS QEMU` image:
    - link: https://fedoraproject.org/coreos/download
    - uncompress the archive:
      - `unxz fedora-coreos-*.qcow2.xz`
- 
