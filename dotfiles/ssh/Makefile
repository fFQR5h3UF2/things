dotfiles/ssh: dotfiles/ssh/personal ## Run ssh/personal

.PHONY: dotfiles/ssh/personal
dotfiles/ssh/personal: dotfiles/setup ## Harden ssh with ssh_server_enabled = false
	$(ANSIBLE_CMD) ./playbook_personal.yml

.PHONY: dotfiles/ssh/server
dotfiles/ssh/server: dotfiles/setup ## Harden ssh with ssh_server_enabled = true
	$(ANSIBLE_CMD)./playbook_server.yml
