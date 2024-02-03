ssh: ssh/personal ## Run ssh/personal

.PHONY: ssh/personal
ssh/personal: setup ## Harden ssh with ssh_server_enabled = false
	$(ANSIBLE_CMD) ./playbook_personal.yml

.PHONY: ssh/server
ssh/server: setup ## Harden ssh with ssh_server_enabled = true
	$(ANSIBLE_CMD)./playbook_server.yml
