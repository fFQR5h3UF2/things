os: os/personal ## Run os/personal

.PHONY: os/personal
os/personal: setup ## Run os hardening with os_desktop_enable = true
	$(ANSIBLE_CMD) "./${PACKAGE}/playbook_personal.yml"

.PHONY: os/server
os/server: ## Run os hardening
	$(ANSIBLE_CMD) "./${PACKAGE}/playbook_server.yml"
