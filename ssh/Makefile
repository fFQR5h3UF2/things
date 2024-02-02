ssh: ssh/personal

.PHONY: ssh/personal
ssh/personal: setup
	$(ANSIBLE_CMD) ./playbook_personal.yml

.PHONY: ssh/server
ssh/server: setup
	$(ANSIBLE_CMD)./playbook_server.yml
