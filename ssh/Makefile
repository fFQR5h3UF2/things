include ../make/common.mk

install: run-playbook-personal

.PHONY: run-playbook-personal
run-playbook-personal: setup
	$(ANSIBLE_CMD) ./playbook_personal.yml

.PHONY: run-playbook-server
run-playbook-server: setup
	$(ANSIBLE_CMD)./playbook_server.yml
