PATH  := $(PATH):$(PWD)/bin:~/.local/bin
SHELL := env PATH=$(PATH) /bin/bash

install_deps:
	pip install -r requirements.txt

run_dev_server:
	flask --app app --debug run

run_prod_server:
	gunicorn app:app
