dotfiles/os: dotfiles/os/personal ## Run os/personal

.PHONY: dotfiles/os/personal
dotfiles/os/personal: dotfiles/setup ## Run os hardening with os_desktop_enable = true
	$(ANSIBLE_CMD) "./${PACKAGE}/playbook_personal.yml"

.PHONY: dotfiles/os/server
dotfiles/os/server: ## Run os hardening
	$(ANSIBLE_CMD) "./${PACKAGE}/playbook_server.yml"
