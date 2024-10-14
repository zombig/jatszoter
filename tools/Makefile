# Determinate absolute path to the repo directory
REPO = $(abspath $(dir $(lastword $(MAKEFILE_LIST)))../)

# Set virtualenv directory param
VENV = $(REPO)/venv
PYTHON = $(VENV)/bin/python

# Temporary files location
TEMP := $(shell mktemp /tmp/jatszoter-bashrc.XXXXXX)

enable:
	@if [ ! -f "$(VENV)/bin/activate" ]; then \
  		echo "ERROR: Unable to find virtual env!"; \
  		echo "ERROR: Please do 'make install' before!"; \
  		exit 1; \
  	fi
	@echo "Starting Jatszoter Developing Environment..."
	@cat $(HOME)/.bashrc $(VENV)/bin/activate > $(TEMP)
	@register-python-argcomplete cz >> $(TEMP)
	@cat $(REPO)/tools/motd
	@/usr/bin/env bash --init-file $(TEMP)
	@rm -v $(TEMP)

uninstall:
	rm -vf $(REPO)/.git/hooks/pre-push
	rm -rf $(VENV)

install: uninstall
	/usr/bin/env python3 -m venv $(VENV)
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r $(REPO)/tools/requirements.txt

update: uninstall install
