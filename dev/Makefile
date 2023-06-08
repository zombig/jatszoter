
REPO_DIR = $(abspath $(dir $(lastword $(MAKEFILE_LIST)))../)

BASE_DIR = $(REPO_DIR)/../venv
PYTHON_DIR = $(BASE_DIR)/python

PYTHON = $(PYTHON_DIR)/bin/python
PC = $(PYTHON_DIR)/bin/pre-commit

TEMP := $(shell mktemp /tmp/jatszoter-bashrc.XXXXXX)

install:
	mkdir -pv $(BASE_DIR)
	/usr/bin/env python3 -m virtualenv $(PYTHON_DIR)
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

uninstall:
	@rm -vf ../.git/hooks/pre-push
	rm -rf $(BASE_DIR)

enable:
	@cat $(HOME)/.bashrc $(PYTHON_DIR)/bin/activate > $(TEMP)
	@register-python-argcomplete cz >> $(TEMP)
	@cat $(REPO_DIR)/dev/motd
	@/usr/bin/env bash --init-file $(TEMP)
	@rm -v $(TEMP)
