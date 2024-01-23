include ../make/common.mk

install: run-playbook
setup: setup-ansible-galaxy

run-playbook: setup
	poetry run ansible-playbook --ask-become-pass -i "127.0.0.1," ./playbook_ssh.yml
